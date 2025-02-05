# Introdução
Este projeto tem como objetivo facilitar as operações de download e upload de arquivos armazenados no 
`Spaces Object Storage` da `Digiral Ocean`

# Pré-requisitos
1. Criar um ambiente virtua Python e ativá-lo
```sh
python3 -m venv venv
```
```sh
source venv/bin/activate
```
2. Instar depêndencias no ambiente virtual isolado
```sh
pip install -r requirements.txt
```

3. Definir seguintes variáveis de ambiente
```sh
# impede a criação de arquivos bytecode .pyc
export PYTHONDONTWRITEBYTECODE=1
# impede que a linguagem faça o buffering de stdout e stderr
export PYTHONUNBUFFERED=1
```

# Variáveis de ambiente requeridas para as operações com os Spaces da DO 
```sh
# região de hospedagem do Bucket/Space. 
export REGION_NAME='sfo3' # exemplo
# endpoint de acesso à região do Bucket/Space 
export ENDPOINT_URL='https://sfo3.digitaloceanspaces.com' # exemplo
# id da chave de acesso
export AWS_ACCESS_KEY_ID='my-key-id'
# chave de acesso
export AWS_SECRET_ACCESS_KEY='my-secret-key'
```

# Para listar os buckets disponíveis
1. Executar o arquivo ```do_bucket_list.py```
```sh
python do_bucket_list.py
```

# Para realizar o download de um diretório na raiz do Bucket
1. Definir variáveis de ambiente necessárias para o download
```sh
# nome do armazenamento (Bucket Name)
export SOURCE_BUCKET='my-bucket'
# nome do diretório na raiz do bucket que deseja baixar
export SOURCE_DIR='my-dir'
```
2. Excutar o arquivo ```do_bucket_download.py```
```sh
python do_bucket_download.py
```
3. O resultado será armazenado no diretório `downloads` que será criado na raiz deste projeto

# Para realizar o upload de um diretório local para a raiz do Bucket
1. Definir variáveis de ambiente necessárias para o upload
```sh
export TARGET_BUCKET='my-bucket'
# nome do diretório de destino que será criado na raiz do bucket
export TARGET_DIR='my-target-dir'
# nome do diretório local que contém os arquivos para upload
export SOURCE_LOCAL_DIR='source-dir-to-upload' 
```
> Ressalta-se que o diretório de upload deve estar dentro da pasta `downloads` na raiz deste projeto

2. Excutar o arquivo ```do_bucket_upload.py```
```sh
python do_bucket_upload.py
```
3. O resultado poderá ser verificado no bucker definido em `TARGET_BUCKET`, disponível na seção ```Spaces Object Storage``` da Digital Ocean

# Referências
- https://medium.com/@tatianatylosky/uploading-files-with-python-using-digital-ocean-spaces-58c9a57eb05b
- https://boto3.amazonaws.com/v1/documentation/api/latest/reference/customizations/s3.html#boto3.s3.transfer.TransferConfig
- https://pythonexamples.org/python-check-if-path-is-file-or-directory/#:~:text=Check%20if%20Given%20Path%20is%20File%20or%20Directory&text=To%20check%20if%20the%20path,if%20it%20is%20a%20directory.
- https://stackoverflow.com/questions/33894197/add-list-of-files-into-a-dictionary-using-python
- https://stackoverflow.com/questions/1602934/check-if-a-given-key-already-exists-in-a-dictionary
- https://gitter.im/boto/boto3?at=5bd19bd6600c5f6423058e4f