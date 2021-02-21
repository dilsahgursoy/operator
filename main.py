sms=int(input("Kullandığınız sms sayısını giriniz."))
data=int(input("Kullandığınız data miktarını giriniz."))

if dk<=1000:
    if sms<=500:
        if data<=5000:
            print(tarife)
            print(tarifeTutarı)
        else:
            print(asımTarifesi)
            print(f"Tarife aşım: {data-5000} mb'tır")
            print("Ödemeniz gereken tutar:",(((data-5000)/100)*5)+30)
    else:
        if data==5000:
            print(asımTarifesi)
            print(f"Tarife aşım:{sms-500} sms'tir.")
            print("Ödemeniz gereken tutar:",((sms-500)*1/2)+30)
        else:
            print(asımTarifesi)
            print(f"Tarife aşım:{sms-500} sms ve {data-5000} mb'tır.")
            print("Ödemeniz gereken tutar:",(((data-5000)/100)*5+((sms-500)*1/2)+30))
            
else:
    if sms>500 and data==5000:
        print(asımTarifesi)
        print(f"Tarife aşım:{dk-1000} dakika ve {sms-500} sms'tir.")
        print("Ödemeniz gereken tutar",(((dk-1000)*1/2)+(sms-500)*1/2)+30)
    elif sms==500 and data>5000:
        print(asımTarifesi)
        print(f"Tarife aşım:{dk-1000} dakika ve {data-5000} mb'tır.")
        print("Ödemeniz gereken tutar:",((dk-1000)*1/2)+(((data-5000)/100)*5)+30)
    elif int(sms)>500 and data>5000:
        print(asımTarifesi)
        print(f"Tarife aşım:{dk-1000} dakika , {data-5000} mb ve {sms-500}sms'tir.")
        print("Ödemeniz gereken tutar:",((dk-500)*1/2)+(sms-500)*1/2)+((((data-5000)/100)*5)+30)
    elif sms==500 and data==5000:
           print(asımTarifesi)
           print(f"Tarife aşım:{dk-1000} dakikadır.")
           print("Ödemeniz gereken tutar:",((dk-1000)*1/2)+30)
