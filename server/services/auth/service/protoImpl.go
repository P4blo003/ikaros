package service

// ------------------------------
// IMPORTS
// ------------------------------
import (
	"context"

	pb "services/auth/service/authpb"
)

// ------------------------------
// IMPLEMENTACIÓN
// ------------------------------

// Servicio a implementar.
type AuthServer struct{}

// Hace el login de usuario. Obtiene las credenciales de la base de datos y comprueba si la constraseña es correcta.
// Si es correcta, genera el JWT y Refresh token.
func (s *AuthServer) Login(ctx context.Context, req *pb.LoginRequest) (*pb.LoginResponse, error) {
	// TODO: Implementar servicio.

	// Retorna la respuesta.
	return &pb.LoginResponse{
		Status:       true,
		AccessToken:  "",
		RefreshToken: "",
	}, nil
}
