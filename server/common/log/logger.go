package log

// ------------------------------
// FUNCIONES
// ------------------------------
import (
	"log"
	"os"
	"time"
)

// ------------------------------
// PARÁMETROS Y VARIABLES
// ------------------------------

// Tipo para el nivel de los logs.
type LogLevel string

// Niveles de severidad de los logs.
const (
	INFO  LogLevel = "INFO"
	DEBUG LogLevel = "DEBUG"
	ERROR LogLevel = "ERROR"
	WARN  LogLevel = "WARN"
)

// ------------------------------
// FUNCIONES
// ------------------------------

// Crea un logger personalizado.
func CreateLogger(name string, level LogLevel) *log.Logger {
	// Crea el prefijo.
	prefix := time.Now().Format("2006/01/02 15:04:05") + " - " + string(level) + " - [" + name + "]: "
	// Crea y retorna el logger.
	return log.New(os.Stdout, prefix, 0)
}
