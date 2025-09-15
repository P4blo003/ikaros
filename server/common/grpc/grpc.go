package common

import (
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

// Crea un nuevo servdor gRPC.
func CreateServer(cfg ServerConfig) (*GrpcServer, error) {
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
