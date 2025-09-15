package service

// ------------------------------
// IMPORTS
// ------------------------------

import (
	"context"
	pb "server/auth/authpb"
)

// ------------------------------
// TIPOS
// ------------------------------
type AuthServer struct {
	pb.UnimplementedAuthServiceServer
}

// ------------------------------
// IMPLEMENTACIÓN
// ------------------------------
func (a *AuthServer) Auth(ctx context.Context, req *pb.AuthReq) (*pb.AuthResp, error) {
	// TODO: Implementar.

	// Retorna la respuesta.
	return &pb.AuthResp{
		Status:       true,
		AccessToken:  "",
		RefreshToken: "",
	}, nil
}
