package main

// ------------------------------
// IMPORTS
// ------------------------------
import (
	"common/log"
)

// ------------------------------
// FLUJO PRINCIPAL
// ------------------------------
func main() {

	// Crea el logger.
	logger := log.CreateLogger("API-GATEWAY", log.INFO)

	// Imprime información.
	logger.Printf("Iniciado servicio PORT: %s", "8080")
}
