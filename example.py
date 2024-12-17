import json
# 将图片文件转换为base64编码
import base64
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.ocr.v20181119 import ocr_client
from OCRRequest import mapping  # 导入 mapping 字典


class TencentOcr(object):
    """
    计费说明：1,000次/月免费
    https://cloud.tencent.com/document/product/866/17619
    """
    SECRET_ID = "自己的账号ID，没有的话先注册"
    SECRET_KEY = "自己的填写一下"
    
    # 地域列表
    # https://cloud.tencent.com/document/api/866/33518#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8
    # 改为广州的节点会快一点
    Region = "ap-guangzhou"

    endpoint = "ocr.tencentcloudapi.com"

    mapping = mapping
    
    def get64Base(self,path):
        with open(path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
            #print(encoded_string)
            with open('myfile.txt', 'w') as f:
                f.write(encoded_string.decode('utf-8'))
        return encoded_string.decode('utf-8')


    def __init__(self):
        cred = credential.Credential(self.SECRET_ID, self.SECRET_KEY)

        httpProfile = HttpProfile()
        httpProfile.endpoint = self.endpoint

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        self.client = ocr_client.OcrClient(cred, self.Region, clientProfile)

    def get_image_text(self, path, ocr):
        req = self.mapping[ocr]()
        req.ImageBase64 = self.get64Base(path)
        #req.ItemNames=["姓名","住址"]
        resp = getattr(self.client, ocr)(req)
        return json.loads(resp.to_json_string())


def main():
    tencentOcr = TencentOcr()
    #填入指定路径下的图片
    url = "test/身份证.png"
    print(tencentOcr.get_image_text(url, "IDCardOCR"))


if __name__ == '__main__':
    main()

