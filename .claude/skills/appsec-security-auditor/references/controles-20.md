# Lista de 20 controles de seguridad AppSec

Para cada control: documentar evidencia (archivo/línea), estado CONFIRMADO/POTENCIAL/SIN EVIDENCIA/NO VERIFICABLE/NO APLICA, criticidad si corresponde, y recomendación verificable. No marcar conforme sin pruebas.

1. **API keys fuera de cliente y código:** revisar variables de entorno, bundles, repositorios, logs y errores; no mostrar valores.
2. **Secretos en historial Git:** inspección autorizada y no destructiva; si se exponen, recomendar rotación y limpieza coordinada del historial.
3. **Claves públicas y permisos DB:** confirmar qué claves pueden exponerse, privilegios mínimos y ausencia de credenciales privilegiadas en frontend.
4. **Row-Level Security:** verificar políticas para aislamiento multiusuario cuando aplique; probar rutas de acceso sin datos reales.
5. **Cifrado de datos sensibles:** cifrado en tránsito y reposo, gestión y rotación de claves según el caso.
6. **Autenticación obligatoria:** rutas, endpoints, websockets, operaciones y recursos protegidos.
7. **Autorización por objeto y registro:** verificar BOLA/IDOR y controles del lado servidor, no solo controles de interfaz.
8. **Protección frente a manipulación de campos:** mass assignment, atributos de roles, propietario, precio, estado y campos internos.
9. **Cookies y sesiones:** Secure, HttpOnly, SameSite, expiración, invalidación, fijación y protección CSRF cuando corresponda.
10. **Contraseñas:** hashing resistente (Argon2id, scrypt o bcrypt configurado correctamente), salt, no almacenamiento reversible.
11. **Rate limiting:** límites por origen/identidad/contexto en autenticación, recuperación, formularios y endpoints costosos.
12. **Bots y abuso:** detección y mitigación proporcional, sin suponer que CAPTCHA resuelve autenticación ni abuso.
13. **Consultas parametrizadas:** SQL/NoSQL, procedimientos y consultas construidas dinámicamente; evitar concatenar entrada.
14. **Validación de entradas:** tipos, esquemas, límites, normalización y controles del servidor.
15. **Sanitización y codificación de salida:** contexto HTML/JS/URL, XSS, plantillas y contenido enriquecido.
16. **Archivos subidos:** tipos permitidos, tamaños, extensiones, verificación de contenido, almacenamiento y acceso seguro.
17. **Minimización de respuestas:** no enviar tokens, PII innecesaria, campos internos o trazas detalladas.
18. **Headers de seguridad:** CSP, HSTS, X-Content-Type-Options, Referrer-Policy y otros según arquitectura.
19. **HTTPS/TLS:** redirecciones, terminación TLS, cookies, certificados y llamadas internas pertinentes.
20. **Dependencias vulnerables:** lockfiles, inventario/SBOM cuando proceda, alertas, mantenimiento y validación de compatibilidad de actualizaciones.

## Criterios de evaluación
- Diferenciar controles ausentes de controles no verificables por acceso incompleto.
- Evaluar la totalidad del flujo: cliente → API → autorización → datos → salida.
- No inferir cumplimiento de RLS por tener autenticación ni inferir seguridad por usar una biblioteca.
- La revisión de dependencias basada en datos no actualizados debe declarar su fecha y limitaciones.
