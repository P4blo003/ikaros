package main

import (
	"log"
	"net"
	"os"
	"os/signal"
	"syscall"

	"google.golang.org/grpc"

	pb "server/auth/authpb"
	"server/auth/service"
)

// ------------------------------
// FLUJO PRINCIPAL
// ------------------------------
func main() {

	// Inicia un puerto de escucha TCP.
	lis, err := net.Listen("tcp", ":50051")

	// Comprueba si se ha abierto correctamente.
	if err != nil {
		log.Fatalf("No se pudo iniciar el servicio gRPC AUTH: %s", err)
	}

	// Inicializa el servidor gRPC.
	grpcServer := grpc.NewServer()
	pb.RegisterAuthServiceServer(grpcServer, &service.AuthServer{})

	// Canal para capturar señales del sistema.
	stop := make(chan os.Signal, 1)
	signal.Notify(stop, os.Interrupt, syscall.SIGTERM)

	go func() {
		log.Println("Auth Service gRPC iniciado en :50051")
		if err := grpcServer.Serve(lis); err != nil {
			log.Fatalf("gRPC failed: %v", err)
		}
	}()

	// Espera la señal de interrupción.
	<-stop
	log.Println("Recibida señal de apagado, cerrando servicio ...")

	// Graceful stop: espera a que terminen llamadas activas
	grpcServer.GracefulStop()
	log.Println("Servidor gRPC detenido correctamente")

}
