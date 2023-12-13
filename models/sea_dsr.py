from app import db

# 30 Inputs
class SEADSR(db.Model):
    # __tablename__ = "sea_dsr"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    sno = db.Column(db.Integer,nullable=False)
    createdby=db.Column(db.String(255),nullable=False)
    createddate=db.Column(db.Date,nullable=False)
    # shipmentmode=db.Column(db.String(255),nullable=True)
    tsvbookingno=db.Column(db.String(255),nullable=False)
    ponumber=db.Column(db.String(255), nullable=False)
    suppliername=db.Column(db.String(255),nullable=False)
    consignee=db.Column(db.String(255),nullable=False)
    materialpickupdate=db.Column(db.Date,nullable=False)
    actualpickupdate=db.Column(db.Date,nullable=False)
    etdcustomer=db.Column(db.Date,nullable=False)
    actualetd=db.Column(db.Date,nullable=False)
    etacustomer=db.Column(db.Date,nullable=False)
    actualeta=db.Column(db.Date,nullable=False)
    countryoforigin=db.Column(db.String(255),nullable=False)
    portofloading=db.Column(db.String(255),nullable=True)
    countryofdestination=db.Column(db.String(255),nullable=False)
    portofdischarge=db.Column(db.String(255),nullable=True)
    containertype=db.Column(db.String(255),nullable=False)
    containertype1=db.Column(db.String(255),nullable=True)
    containertype2=db.Column(db.String(255),nullable=True)
    noofcontainers=db.Column(db.Integer,nullable=False)
    containernumbers=db.Column(db.String(255),nullable=False)
    netwt = db.Column(db.String(255), nullable=False)
    grswt = db.Column(db.String(255), nullable=False)
    chgwt = db.Column(db.String(255), nullable=False)
    pkgs = db.Column(db.Integer, nullable=False)
    packagetype=db.Column(db.String(255),nullable=False)
    commodity=db.Column(db.String(255),nullable=False)
    mblnumber=db.Column(db.String(255),nullable=False)
    hblnumber=db.Column(db.String(255),nullable=False)
    shippingliner=db.Column(db.String(255),nullable=False)
    vesselvoyage=db.Column(db.String(255),nullable=False)
    firstfeedername=db.Column(db.String(255),nullable=False)
    firstfeederimono=db.Column(db.String(255),nullable=False)
    transhipment1steta=db.Column(db.Date,nullable=False)
    transhipment1stetd=db.Column(db.Date,nullable=False)
    transhipment1stportname=db.Column(db.String(255),nullable=False)
    mothervesselname=db.Column(db.String(255),nullable=False)
    mothervesselimono=db.Column(db.String(255),nullable=False)
    mothervesseleta=db.Column(db.Date,nullable=False)
    mothervesseletd=db.Column(db.Date,nullable=False)
    mothervesselportname=db.Column(db.String(255),nullable=False)
    secondfeedername=db.Column(db.String(255),nullable=False)
    secondfeederimono=db.Column(db.String(255),nullable=False)
    transhipment2ndeta=db.Column(db.Date,nullable=False)
    transhipment2ndetd=db.Column(db.Date,nullable=False)
    transhipment2ndportname=db.Column(db.String(255),nullable=False)
    thirdfeedername=db.Column(db.String(255),nullable=True)
    thirdfeederimono=db.Column(db.String(255),nullable=True)
    transhipment3rdeta=db.Column(db.Date,nullable=True)
    transhipment3rdetd=db.Column(db.Date,nullable=True)
    transhipment3rdportname=db.Column(db.String(255),nullable=True)
    prealertdtd=db.Column(db.Date,nullable=False)
    remarks=db.Column(db.String(255),nullable=False)
    updatedby=db.Column(db.String(255),nullable=False)
    updateddate=db.Column(db.Date,nullable=False)


    def __init__(self,sno,createdby,createddate,tsvbookingno,ponumber,suppliername,consignee,materialpickupdate,actualpickupdate,etdcustomer,actualetd,etacustomer,actualeta,countryoforigin,portofloading,countryofdestination,portofdischarge,containertype,containertype1,containertype2,noofcontainers,containernumbers,netwt,grswt,chgwt,pkgs,packagetype,commodity,mblnumber,hblnumber,shippingliner,vesselvoyage,firstfeedername,firstfeederimono,transhipment1steta,transhipment1stetd,transhipment1stportname,mothervesselname,mothervesselimono,mothervesseleta,mothervesseletd,mothervesselportname,secondfeedername,secondfeederimono,transhipment2ndeta,transhipment2ndetd,transhipment2ndportname,thirdfeedername,thirdfeederimono,transhipment3rdeta,transhipment3rdetd,transhipment3rdportname,prealertdtd,remarks,updatedby,updateddate):
        self.sno=sno
        self.createdby=createdby
        self.createddate=createddate
        # self.shipmentmode=shipmentmode
        self.tsvbookingno=tsvbookingno
        self.ponumber=ponumber
        self.suppliername=suppliername
        self.consignee=consignee
        self.materialpickupdate=materialpickupdate
        self.actualpickupdate=actualpickupdate
        self.etdcustomer=etdcustomer
        self.actualetd=actualetd
        self.etacustomer=etacustomer
        self.actualeta=actualeta
        self.countryoforigin=countryoforigin
        self.portofloading=portofloading
        self.countryofdestination=countryofdestination
        self.portofdischarge=portofdischarge
        self.containertype=containertype
        self.containertype1=containertype1
        self.containertype2=containertype2
        self.noofcontainers=noofcontainers
        self.containernumbers=containernumbers
        self.netwt=netwt
        self.grswt=grswt
        self.chgwt=chgwt
        self.pkgs=pkgs
        self.packagetype=packagetype
        self.commodity=commodity
        self.mblnumber=mblnumber
        self.hblnumber=hblnumber
        self.shippingliner=shippingliner
        self.vesselvoyage=vesselvoyage
        self.firstfeedername=firstfeedername
        self.firstfeederimono=firstfeederimono
        self.transhipment1steta=transhipment1steta
        self.transhipment1stetd=transhipment1stetd
        self.transhipment1stportname=transhipment1stportname
        self.mothervesselname=mothervesselname
        self.mothervesselimono=mothervesselimono
        self.mothervesseleta=mothervesseleta
        self.mothervesseletd=mothervesseletd
        self.mothervesselportname=mothervesselportname
        self.secondfeedername=secondfeedername
        self.secondfeederimono=secondfeederimono
        self.transhipment2ndeta=transhipment2ndeta
        self.transhipment2ndetd=transhipment2ndetd
        self.transhipment2ndportname=transhipment2ndportname
        self.thirdfeedername=thirdfeedername
        self.thirdfeederimono=thirdfeederimono
        self.transhipment3rdeta=transhipment3rdeta
        self.transhipment3rdetd=transhipment3rdetd
        self.transhipment3rdportname=transhipment3rdportname
        self.prealertdtd=prealertdtd
        self.remarks=remarks
        self.updatedby=updatedby
        self.updateddate=updateddate



    # Custom methods for business logic (if any) can be added here.

