# Revisiones complementarias

Marco orientador: OWASP Top 10:2025 y OWASP ASVS 5.0. Citar identificadores exactos de ASVS solo si están verificados en la versión utilizada.

- Inventario de activos, endpoints y límites de confianza; revisión de arquitectura y dependencias críticas.
- Errores de control de acceso (horizontal y vertical), escalada de privilegios y fallas de segregación multiusuario.
- Autenticación, MFA, recuperación de cuenta, cierre de sesión, revocación y tokenización.
- Gestión de secretos en CI/CD, contenedores, entornos, repositorios y registros.
- Riesgos de SSRF, inyección, deserialización insegura, ejecución de comandos y rutas de archivos.
- Configuraciones erróneas de CORS, proxy, caché, almacenamiento, cloud, cabeceras y origen confiable.
- Seguridad de APIs: BOLA, BFLA, exceso de datos, enumeración, consumo descontrolado de recursos y esquemas de entrada/salida.
- Cadena de suministro: dependencias, acciones CI/CD, versiones fijadas, integridad, revisiones y privilegios del pipeline.
- Registro y monitoreo: eventos críticos, retención, integridad, privacidad, alertas y respuesta a incidentes.
- Lógica de negocio, condiciones de carrera, transacciones, antifraude y operaciones sensibles.
- Protecciones específicas para PHP, Python/FastAPI, Node, SQL/MariaDB, aplicaciones móviles y otras tecnologías detectadas.
- Privacidad por diseño: minimización, retención, accesos y tratamiento apropiado de datos.
- Pruebas seguras: unitarias, de integración, SAST/SCA y DAST **solo** cuando esté autorizado y con límites definidos.

Los controles no aplicables deben explicarse; los inaccesibles deben figurar como NO VERIFICABLE.
