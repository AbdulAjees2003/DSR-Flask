from app import db  # Importing the db instance from your main app file

class AIRDSR(db.Model):
    # __tablename__ = "air_dsr"  # Explicitly naming the table
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sno = db.Column(db.Integer,nullable=False)
    createdby=db.Column(db.String(255),nullable=False)
    createddate=db.Column(db.Date,nullable=False)
    tsvbookingno=db.Column(db.String(255),nullable=False)
    ponumber = db.Column(db.String(255), nullable=False)  # Ensuring ponumber is not nullable
    suppliername = db.Column(db.String(255), nullable=False)
    consignee = db.Column(db.String(255), nullable=False)
    bookingreceiveddate = db.Column(db.Date, nullable=False)
    bkgdate = db.Column(db.Date, nullable=False)
    cargoreadiness = db.Column(db.Date, nullable=False)
    pickupdate = db.Column(db.Date, nullable=False)
    warehousercvd = db.Column(db.Date, nullable=False)
    countryoforigin=db.Column(db.String(255),nullable=False)
    portofloading=db.Column(db.String(255),nullable=True)
    countryofdestination=db.Column(db.String(255),nullable=False)
    portofdischarge=db.Column(db.String(255),nullable=True)
    terms = db.Column(db.String(255), nullable=False)
    hawbno = db.Column(db.String(255), nullable=False)
    mawbno = db.Column(db.String(255), nullable=False)
    netwt = db.Column(db.String(255), nullable=False)
    grswt = db.Column(db.String(255), nullable=False)
    chgwt = db.Column(db.String(255), nullable=False)
    pkgs = db.Column(db.Integer, nullable=False)
    packagetype=db.Column(db.String(255),nullable=False)
    commodity=db.Column(db.String(255),nullable=False)
    flight1 = db.Column(db.String(255), nullable=False)
    flight2 = db.Column(db.String(255), nullable=True)
    flight3 = db.Column(db.String(255), nullable=True)
    etd = db.Column(db.Date, nullable=False)
    eta = db.Column(db.Date, nullable=False)
    revisedetd = db.Column(db.Date, nullable=False)
    revisedeta = db.Column(db.Date, nullable=False)
    prealertdtd = db.Column(db.Date, nullable=False)
    remarks = db.Column(db.String(255), nullable=False)
    updatedby=db.Column(db.String(255),nullable=False)
    updateddate=db.Column(db.Date,nullable=False)


    def __init__(self,sno,createdby,createddate,tsvbookingno,ponumber,suppliername,consignee,bookingreceiveddate,bkgdate,cargoreadiness,pickupdate,warehousercvd,countryoforigin,portofloading,countryofdestination,portofdischarge,terms,hawbno,mawbno,netwt,grswt,chgwt,pkgs,packagetype,commodity,flight1,flight2,flight3,etd,eta,revisedetd,revisedeta,prealertdtd,remarks,updatedby,updateddate):
        self.sno=sno
        self.createdby=createdby
        self.createddate=createddate
        self.tsvbookingno=tsvbookingno
        self.ponumber=ponumber
        self.suppliername=suppliername
        self.consignee=consignee
        self.bookingreceiveddate=bookingreceiveddate
        self.bkgdate=bkgdate
        self.cargoreadiness=cargoreadiness
        self.pickupdate=pickupdate
        self.warehousercvd=warehousercvd
        self.countryoforigin=countryoforigin
        self.portofloading=portofloading
        self.countryofdestination=countryofdestination
        self.portofdischarge=portofdischarge
        self.terms=terms
        self.hawbno=hawbno
        self.mawbno=mawbno
        self.netwt=netwt
        self.grswt=grswt
        self.chgwt=chgwt
        self.pkgs=pkgs
        self.packagetype=packagetype
        self.commodity=commodity
        self.flight1=flight1
        self.flight2=flight2
        self.flight3=flight3
        self.etd=etd
        self.eta=eta
        self.revisedetd=revisedetd
        self.revisedeta=revisedeta
        self.prealertdtd=prealertdtd
        self.remarks=remarks
        self.updatedby=updatedby
        self.updateddate=updateddate


    # Custom methods for business logic (if any) can be added here.
