# 假设这些请求类已经定义好了，并且可以从某个模块中导入
# 这里使用占位符类名作为示例
from tencentcloud.ocr.v20181119.models import (
    AdvertiseOCRRequest,
    GeneralBasicOCRRequest,
    ImageEnhancementRequest,
    RecognizeHealthCodeOCRRequest,
    RecognizeTravelCardOCRRequest,
    GeneralAccurateOCRRequest,
    GeneralEfficientOCRRequest,
    GeneralFastOCRRequest,
    EnglishOCRRequest,
    GeneralHandwritingOCRRequest,
    TextDetectRequest,
    # 卡证文字识别相关请求类
    BankCardOCRRequest,
    BizLicenseOCRRequest,
    BusinessCardOCRRequest,
    ClassifyDetectOCRRequest,
    EnterpriseLicenseOCRRequest,
    EstateCertOCRRequest,
    HKIDCardOCRRequest,
    HmtResidentPermitOCRRequest,
    IDCardOCRRequest,
    InstitutionOCRRequest,
    MLIDCardOCRRequest,
    MLIDPassportOCRRequest,
    MainlandPermitOCRRequest,
    OrgCodeCertOCRRequest,
    PassportOCRRequest,
    PermitOCRRequest,
    PropOwnerCertOCRRequest,
    # 票据单据识别相关请求类
    BankSlipOCRRequest,
    BusInvoiceOCRRequest,
    CarInvoiceOCRRequest,
    DutyPaidProofOCRRequest,
    FinanBillOCRRequest,
    FinanBillSliceOCRRequest,
    FlightInvoiceOCRRequest,
    InvoiceGeneralOCRRequest,
    MixedInvoiceDetectRequest,
    MixedInvoiceOCRRequest,
    QuotaInvoiceOCRRequest,
    RecognizeContainerOCRRequest,
    RecognizeMedicalInvoiceOCRRequest,
    RecognizeOnlineTaxiItineraryOCRRequest,
    ShipInvoiceOCRRequest,
    TaxiInvoiceOCRRequest,
    TollInvoiceOCRRequest,
    TrainTicketOCRRequest,
    VatInvoiceOCRRequest,
    VatRollInvoiceOCRRequest,
    VerifyOfdVatInvoiceOCRRequest,
    WaybillOCRRequest,
    # 汽车场景识别相关请求类
    DriverLicenseOCRRequest,
    LicensePlateOCRRequest,
    RideHailingDriverLicenseOCRRequest,
    RideHailingTransportLicenseOCRRequest,
    VehicleLicenseOCRRequest,
    VehicleRegCertOCRRequest,
    VinOCRRequest,
    # 行业文档识别相关请求类
    RecognizeTableOCRRequest,  # 注意版本V2
    ArithmeticOCRRequest,
    EduPaperOCRRequest,
    FormulaOCRRequest,
    InsuranceBillOCRRequest,
    SealOCRRequest,
    SmartStructuralOCRRequest,
    SmartStructuralOCRV2Request,
    TableOCRRequest,  # 注意版本V1

)
 
# 接口名称到请求类的映射
mapping = {
    #综合识别
    "SmartStructuralOCRV2": SmartStructuralOCRV2Request,
    # 通用文字识别相关接口
    "AdvertiseOCR": AdvertiseOCRRequest,
    "GeneralBasicOCR": GeneralBasicOCRRequest,
    "ImageEnhancement": ImageEnhancementRequest,
    "RecognizeHealthCodeOCR": RecognizeHealthCodeOCRRequest,
    "RecognizeTravelCardOCR": RecognizeTravelCardOCRRequest,
    "GeneralAccurateOCR": GeneralAccurateOCRRequest,
    "GeneralEfficientOCR": GeneralEfficientOCRRequest,
    "GeneralFastOCR": GeneralFastOCRRequest,
    "EnglishOCR": EnglishOCRRequest,
    "GeneralHandwritingOCR": GeneralHandwritingOCRRequest,
    "TextDetect": TextDetectRequest,
    
    # 卡证文字识别相关接口
    "BankCardOCR": BankCardOCRRequest,
    "BizLicenseOCR": BizLicenseOCRRequest,
    "BusinessCardOCR": BusinessCardOCRRequest,
    "ClassifyDetectOCR": ClassifyDetectOCRRequest,
    "EnterpriseLicenseOCR": EnterpriseLicenseOCRRequest,
    "EstateCertOCR": EstateCertOCRRequest,
    "HKIDCardOCR": HKIDCardOCRRequest,
    "HmtResidentPermitOCR": HmtResidentPermitOCRRequest,
    "IDCardOCR": IDCardOCRRequest,
    "InstitutionOCR": InstitutionOCRRequest,
    "MLIDCardOCR": MLIDCardOCRRequest,
    "MLIDPassportOCR": MLIDPassportOCRRequest,
    "MainlandPermitOCR": MainlandPermitOCRRequest,
    "OrgCodeCertOCR": OrgCodeCertOCRRequest,
    "PassportOCR": PassportOCRRequest,
    "PermitOCR": PermitOCRRequest,
    "PropOwnerCertOCR": PropOwnerCertOCRRequest,

    
    # 票据单据识别相关接口
    "BankSlipOCR": BankSlipOCRRequest,
    "BusInvoiceOCR": BusInvoiceOCRRequest,
    "CarInvoiceOCR": CarInvoiceOCRRequest,
    "DutyPaidProofOCR": DutyPaidProofOCRRequest,
    "FinanBillOCR": FinanBillOCRRequest,
    "FinanBillSliceOCR": FinanBillSliceOCRRequest,
    "FlightInvoiceOCR": FlightInvoiceOCRRequest,
    "InvoiceGeneralOCR": InvoiceGeneralOCRRequest,
    "MixedInvoiceDetect": MixedInvoiceDetectRequest,
    "MixedInvoiceOCR": MixedInvoiceOCRRequest,
    "QuotaInvoiceOCR": QuotaInvoiceOCRRequest,
    "RecognizeContainerOCR": RecognizeContainerOCRRequest,
    "RecognizeMedicalInvoiceOCR": RecognizeMedicalInvoiceOCRRequest,
    "RecognizeOnlineTaxiItineraryOCR": RecognizeOnlineTaxiItineraryOCRRequest,
    "ShipInvoiceOCR": ShipInvoiceOCRRequest,
    "TaxiInvoiceOCR": TaxiInvoiceOCRRequest,
    "TollInvoiceOCR": TollInvoiceOCRRequest,
    "TrainTicketOCR": TrainTicketOCRRequest,
    "VatInvoiceOCR": VatInvoiceOCRRequest,
    "VatRollInvoiceOCR": VatRollInvoiceOCRRequest,
    "VerifyOfdVatInvoiceOCR": VerifyOfdVatInvoiceOCRRequest,
    "WaybillOCR": WaybillOCRRequest,
    
    # 汽车场景识别相关接口
    "DriverLicenseOCR": DriverLicenseOCRRequest,
    "LicensePlateOCR": LicensePlateOCRRequest,
    "RideHailingDriverLicenseOCR": RideHailingDriverLicenseOCRRequest,
    "RideHailingTransportLicenseOCR": RideHailingTransportLicenseOCRRequest,
    "VehicleLicenseOCR": VehicleLicenseOCRRequest,
    "VehicleRegCertOCR": VehicleRegCertOCRRequest,
    "VinOCR": VinOCRRequest,
    
    # 行业文档识别相关接口
    "RecognizeTableOCR": RecognizeTableOCRRequest,  # 注意版本V2
    "ArithmeticOCR": ArithmeticOCRRequest,
    "EduPaperOCR": EduPaperOCRRequest,
    "FormulaOCR": FormulaOCRRequest,
    "InsuranceBillOCR": InsuranceBillOCRRequest,
    "SealOCR": SealOCRRequest,
    "SmartStructuralOCR": SmartStructuralOCRRequest,
    "TableOCR": TableOCRRequest,  # 注意版本V1

}