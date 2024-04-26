# Repository Information

This is a repository about the conception of Private Cloud.
## Requirement
There are some requirements before using the app. In the file `requirements.md`, you will see some element you need to do.

## How to run the server :
Every time you modify something in the **swagger** directory. You need to run this command :
```bash
cd SRC/swagger
swagger-cli bundle swagger.yml --outfile openapi.yml --type yaml
```

```bash
cd SRC
python .\main.py
```
 Then go to : http://HOST:PORT/v1/ui