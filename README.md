# curso-odoo-v14

Módulo `peliculas` del curso básico de Odoo 14.

La raíz de este repositorio **es** el módulo, así que se clona con el nombre
técnico dentro de la carpeta de addons de Odoo:

    git clone https://github.com/samolina-cmd/curso-odoo-v14.git peliculas

## Reglas

- `14.0` es la rama aprobada. Nadie sube directo a ella: todo entra por Pull Request.
- Cada quien trabaja en su propia rama: `14.0-nombre`, por ejemplo `14.0-cristian`.
- Antes de abrir el PR, trae `14.0` a tu rama y resuelve ahí los conflictos.
- Sebastián Molina revisa y hace el merge.

## Lo que nunca se sube

| Qué | Por qué |
|---|---|
| `__pycache__/`, `*.pyc` | Los genera Python en cada ejecución; se recrean solos |
| `*.log` | Son de tu máquina y cambian todo el tiempo |
| `.idea/`, `.vscode/` | Configuración de tu editor, no del módulo |
| `odoo.conf` | Lleva rutas y contraseñas locales |

## Flujo de trabajo

Crear tu rama y subirla la primera vez:

    git switch -c 14.0-tunombre
    git add <archivos>
    git commit -m "Lo que hiciste"
    git push -u origin 14.0-tunombre

En GitHub aparece el botón **Compare & pull request**. Lo abres contra `14.0`,
describes qué hiciste y esperas la revisión.

Después del primer push, en los siguientes basta con `git push`.

Antes de abrir el PR, traer lo aprobado:

    git switch 14.0
    git pull
    git switch 14.0-tunombre
    git merge 14.0

Si Git reporta conflicto, se resuelve en tu rama, nunca en `14.0`.

## Comandos de consulta

| Comando | Para qué |
|---|---|
| `git status` | Qué cambió y qué está listo para el commit |
| `git branch` | En qué rama estás y cuáles tienes |
| `git log --oneline` | Historial de commits, uno por línea |
| `git diff` | Qué cambiaste frente al último commit |
