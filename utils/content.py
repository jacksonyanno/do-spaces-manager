import os

# Dicionário com mapeamento da extenssão do arquivo para o tipo de arquivo armazenado no Spaces da DO

CONTENT_TYPE_DICT = {
    '':      'application/octet-stream',
    '.pdf':  'application/pdf',
    '.json': 'application/json',
    '.eot':  'application/vnd.ms-fontobject',
    '.ttf':  'font/ttf',
    '.woff': 'font/woff',
    '.woff2':'font/woff2',
    '.html': 'text/html',
    '.css':  'text/css',
    '.js':   'text/javascript',
    '.xml':  'text/xml',
    '.md':   'text/markdown',
    '.txt':  'text/plain',
    '.ico':  'image/vnd.microsoft.icon',
    '.svg':  'image/svg+xml',
    '.jpg':  'image/jpg',
    '.jpeg': 'image/jpeg',
    '.png':  'image/png',
    '.webp': 'image/webp',
}
