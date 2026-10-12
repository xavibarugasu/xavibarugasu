# AppSec Security Auditor v1.1 — Instalación

**Autor y responsable del proyecto:** Javier Enrique Vargas Carrasco  
**Profesión:** Ingeniero en Informática, mención en Ciberseguridad  
**© 2026 Javier Enrique Vargas Carrasco. Todos los derechos reservados.**

## Instalación en Claude Code
La skill ya está alojada en `.claude/skills/appsec-security-auditor/` de este repositorio. Al trabajar directamente en este repositorio con Claude Code, puede ser detectada por contexto. Para usarla en **otro** proyecto, copia la carpeta de la skill a `.claude/skills/` de ese proyecto, o instálala en el directorio de skills de usuario según la versión de Claude Code.

Para una política recurrente, copia o adapta el contenido de `references/INSTRUCCIONES-PROYECTO.md` al archivo `CLAUDE.md` del proyecto de destino. Evita sobreescribir instrucciones existentes sin revisarlas.

## Uso
- Automático contextual: Claude decide cargar la skill al trabajar con superficies sensibles.
- Explícito: «Usa appsec-security-auditor en modalidad AUDITAR para revisar este proyecto y elaborar un informe, sin modificar archivos».
- Remediación: «Propón un plan de corrección; espera mi aprobación antes de editar».

## Advertencias
GitHub aloja la skill, pero no ejecuta tareas ni auditorías por sí mismo. La publicación en GitHub **no instala** automáticamente la skill en todos tus proyectos. No equivale a una evaluación de seguridad certificada. Para verificaciones al hacer push es necesaria una configuración CI/CD independiente.

## Atribución
Skill preparada como proyecto de Javier Enrique Vargas Carrasco con asistencia de inteligencia artificial, sobre referencias técnicas externas, incluidas OWASP Top 10 y OWASP ASVS. No se atribuye autoría sobre esos estándares.
