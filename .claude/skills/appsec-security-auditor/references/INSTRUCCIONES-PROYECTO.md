# Instrucciones persistentes para Claude Code / Proyectos Claude

Cuando una tarea implique código, API, autenticación, permisos, formularios, consultas, almacenamiento, secretos, configuración, dependencias o despliegues, usa la skill `appsec-security-auditor` para efectuar una revisión de seguridad contextual del cambio. No afirmes haber auditado todo el proyecto por realizar una revisión parcial.

Si se solicita una auditoría completa, usa modalidad AUDITAR en solo lectura con los 20 controles y OWASP como referencias. Si se solicita planificación, usa PLAN. Antes de CORREGIR vulnerabilidades, presenta un diff o plan concreto y pide autorización. Comunica pruebas realizadas y no realizadas. Nunca expongas secretos ni hagas pruebas activas en producción sin autorización y alcance definido.

Esta política se aplica durante las sesiones de trabajo con Claude. No habilita tareas autónomas programadas ni monitorización permanente.
