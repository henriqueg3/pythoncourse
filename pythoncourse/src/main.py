'''
Created on 9 de mar de 2017
Alterado em 16 de mar de 2017
@author: Gilzamir Gomes
'''

# coding: utf-8

import io
import sys
import urllib.request as request
import zipfile
import utils as dw
import os

def loadlistfromcsv():
    RESOURCE_URL = "http://repositorio.dados.gov.br/saude/unidades-saude/unidade-basica-saude/ubs.csv.zip"
    OUTPUT_PATH = "C:/Users/Henrique/saida.zip"
    EXTRACTED_PATH = "C:/Users/Henrique/" 
    if len(sys.argv) > 1:
        RESOURCE_URL = sys.argv[1] 
    if len(sys.argv) > 2:
        OUTPUT_PATH = sys.argv[2]
    if len(sys.argv) > 3:
        EXTRACTED_PATH = sys.argv[3]
    response = request.urlopen(RESOURCE_URL)
    out_file = io.FileIO(OUTPUT_PATH, mode="w")
    content_length = response.getheader('Content-Length')
    if content_length:
        length = int(content_length)
        dw.download_length(response, out_file, length)
    else:
        dw.download(response, out_file)
    zfile = zipfile.ZipFile(OUTPUT_PATH)
    zfile.extractall(EXTRACTED_PATH)
    
    filename = [name for name in os.listdir(EXTRACTED_PATH) if '.csv' in name]
    
    print(filename)
    
    dt = dw.read_data(EXTRACTED_PATH+filename[0])

    #print(dw.extract_filename('cavalo.de.troia.ua'))

    return dt

def main():
    list = loadlistfromcsv() 
    Args = ['cod_munic', 'cod_cnes']
    dicionario = dw.create_index_from(list, {"cod_munic":2, 'cod_cnes':3}, *Args) 
    
    for i in dicionario:
        print(i, dicionario[i])
        
    
if __name__ == "__main__":
    main()