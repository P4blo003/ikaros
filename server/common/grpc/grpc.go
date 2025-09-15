package common

import (
	"context"
	"log"
	"net"
	"strconv"
	"time"

	"google.golang.org/grpc"
)

// ------------------------------
// TIPOS
// ------------------------------

// Contiene la confuguración del servidor gRPC.
type ServerConfig struct {
	// Puerto del servidor gRPC.
	Port int
	// Nombre del servicio del servidor.
	ServiceName string
	// Máximo tiempo de espera hasta apagar forzosamente.
	MaxShutdownTime time.Duration
}

// Contiene el servidor con toda la funcionalidad.
type GrpcServer struct {
	// Servidor gRPC.
	Server *grpc.Server
	// Canal de escucha del servidor gRPC.
	Listener net.Listener
	// Configuración del servidor gRPC.
	Config ServerConfig
}

// ------------------------------
// FUNCIONES
// ------------------------------

// Inicializa un nuevo servidor gRPC.
func InitServer(cfg ServerConfig) (*GrpcServer, error) {
	// Genera la dirección.
	addr := "localhost:" + strconv.Itoa(cfg.Port)

	// Crea el canal de escucha.
	lis, err := net.Listen("tcp", addr)
	// Comprueba si se inición con éxito.
	if err != nil {
		// Retorna el error.
		return nil, err
	}

	// Crea el servidor gRPC.
	s := grpc.NewServer()

	// Retorna el servidor completo.
	return &GrpcServer{
		Server:   s,
		Listener: lis,
		Config:   cfg,
	}, nil
}

// ------------------------------
// IMPLEMENTACIÓN
// ------------------------------

// Inicia el servidor gRPC.
func (s *GrpcServer) Start() {
	// Inicia gorutina.
	go func() {
		// Imprime información.
		log.Printf("[%s] Servidor iniciado en %s", s.Config.ServiceName, s.Listener.Addr().String())
		// Inicia el servicio en el puerto dado.
		if err := s.Server.Serve(s.Listener); err != nil {
			log.Printf("[%s] Error en servidor: %v", s.Config.ServiceName, err)
		}
	}()
}

// Detiene el servidor gRPC.
func (s *GrpcServer) Stop() {
	// Imprime información.
	log.Printf("[%s] Iniciando apagado controlado...", s.Config.ServiceName)

	// Crea un contexto con timeout.
	ctx, cancel := context.WithTimeout(context.Background(), s.Config.MaxShutdownTime)
	// Asegura que al salir de la función se liberen los recursos asociados.
	defer cancel()

	// Crea un canal sin buffer. Se usará como señal para indicar cuándo GracefulStop haya terminado.
	done := make(chan struct{})
	// Lanza gorutina.
	go func() {
		// Permite que las llamadas gRPC activas terminen.
		s.Server.GracefulStop()
		// Cierra el canal.
		close(done)
	}()

	// Select para dos posibles casos.
	select {
	// Apagado ordenado.
	case <-done:
		// Imprime información.
		log.Printf("[%s] Servidor detenido correctamente", s.Config.ServiceName)
	// Apadado forzoso. (Si el timeout termina antes que la gorutina).
	case <-ctx.Done():
		// Imprime información.
		log.Printf("[%s] Timeout, forzando cierre...", s.Config.ServiceName)
		// Detiene el servidor gRPC forzosamente.
		s.Server.Stop()
	}
}
