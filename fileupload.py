from urllib3 import encode_multipart_formdata
import requests
 
def post_files(url,header,data,filename,filepath):
    """
        :param files: (optional) Dictionary of ``'name': file-like-objects`` (or ``{'name': file-tuple}``) for multipart encoding upload.
        ``file-tuple`` can be a 2-tuple ``('filename', fileobj)``, 3-tuple ``('filename', fileobj, 'content_type')``
        or a 4-tuple ``('filename', fileobj, 'content_type', custom_headers)``, where ``'content-type'`` is a string
        defining the content type of the given file and ``custom_headers`` a dict-like object containing additional headers
        to add for the file.
    """
    data['file']= (filename,open(filepath,'rb').read())
    encode_data = encode_multipart_formdata(data)
    data = encode_data[0]
    header['Content-Type'] = encode_data[1]
    r = requests.post(url, headers=header, data=data)
    print(r.content)
 
if __name__=="__main__":
    #url,filename,filepath string
    #header,data dict
    print(post_files("url",{"header":"value"},{"data":"value"},"filename","filepath"))