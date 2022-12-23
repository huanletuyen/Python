import calendar
#import datetime
#import subprocess
print("day la chuong trinh tu dong gen code theo nam, hay thuc hien cac thao tac sau:")
#print("1: hay nhap nam can gen code theo dinh dang yyyy:")
#year = input()
print("1: nhap ngay bat dau can gen code theo dinh dang yyyymmdd:")
start_day = input()
print("2: nhap ngay ket thuc can gen code theo dinh dang yyyymmdd:")
end_day = input()
print("========================GENETATING GEN CODE ========================")
start_month = start_day[4:6]
end_month = end_day[4:6]
start_year = start_day[0:4]
end_year = end_day[0:4]
def gencode(gendcode_year,gencode_month,gencode_sum_day, gencode_start_day_of_month, gencode_subtrahend_day):
    for day in range(int(gencode_start_day_of_month), int(gencode_sum_day) + 1 - int(gencode_subtrahend_day)):
        if int(gencode_month) < 10:
            month_string = "0" + str(gencode_month)
        else:
            month_string = str(gencode_month)
        if int(day) < 10:
            day_string = "0" + str(day)
        else:
            day_string = str(day)
        if int(day) < int(sum_day) + 1:
            year_month_day = str(gendcode_year) + month_string + day_string
            print(year_month_day)
            file = open("./command.sh", "a+")
            data = "curl --location --request POST 'http://localhost:4200/app/info_sky_v2/blocking/job/log_bhxh_end_record' --header 'Content-Type: application/json'" + " --data " + str("'{") +str('"day":"') + year_month_day.rstrip() +str('"}') + "'" + "\n"
            file.writelines(data)
            file.close()
for year in range(int(start_year),int(end_year) + 1):
    if int(year) != int(start_year) and int(year) != int(end_year):
        for month in range(1,13):
            sum_day = calendar.monthrange(int(year), int(month))[1]
            start_day_of_month = int(1)
            subtrahend_day = int(0)
            gencode(year,month,sum_day,start_day_of_month,subtrahend_day)
    elif int(year) == int(start_year) and int(year) == int(end_year):
        if int(start_month) == int(end_month):
            sum_day = calendar.monthrange(int(year), int(start_month))[1]
            start_day_of_month = int(start_day[6:8])
            subtrahend_day = int(sum_day) - int(end_day[6:8])
            gencode(year,month,sum_day,start_day_of_month,subtrahend_day)
        else:
            for month in range(int(start_month), int(end_month) + 1):
                if int(month) == int(start_month):
                    sum_day = calendar.monthrange(int(year), int(month))[1]
                    start_day_of_month = int(start_day[6:8])
                    subtrahend_day = int(0)
                    gencode(year,month,sum_day,start_day_of_month,subtrahend_day)
                elif int(month) == int(end_month):
                    sum_day = calendar.monthrange(int(year), int(month))[1]
                    start_day_of_month = int(1)
                    subtrahend_day = int(sum_day) - int(end_day[6:8])
                    gencode(year,month,sum_day,start_day_of_month,subtrahend_day)
                else:
                    sum_day = calendar.monthrange(int(year), int(month))[1]
                    start_day_of_month = int(1)
                    subtrahend_day = int(0)
                    gencode(year,month,sum_day,start_day_of_month,subtrahend_day)
    elif int(year) == int(start_year) or int(year) == int(end_year):
        # int(year) == int(start_year) or int(year) == int(end_year):
        if int(year) == int(start_year):
            for month in range(int(start_month), 13):
                if int(month) == int(start_month):
                    sum_day = calendar.monthrange(int(year), int(month))[1]
                    start_day_of_month = int(start_day[6:8])
                    subtrahend_day = int(0)
                    gencode(year,month,sum_day,start_day_of_month,subtrahend_day)
                else:
                    sum_day = calendar.monthrange(int(year), int(month))[1]
                    start_day_of_month = int(1)
                    subtrahend_day = int(0)
                    gencode(year,month,sum_day,start_day_of_month,subtrahend_day)
        elif int(year) == int(end_year):
            for month in range(1, int(end_month) +1 ):
                if int(month) == int(end_month):
                    sum_day = calendar.monthrange(int(year), int(month))[1]
                    start_day_of_month = int(1)
                    subtrahend_day = int(sum_day) - int(end_day[6:8])
                    gencode(year,month,sum_day,start_day_of_month,subtrahend_day)
                else:
                    sum_day = calendar.monthrange(int(year), int(month))[1]
                    start_day_of_month = int(1)
                    subtrahend_day = int(0)
                    gencode(year,month,sum_day,start_day_of_month,subtrahend_day)
        else:
            sum_day = calendar.monthrange(int(year), int(month))[1]
            start_day_of_month = int(1)
            subtrahend_day = int(0)
            gencode(year,month,sum_day,start_day_of_month,subtrahend_day)
print("========================GENETATED GEN CODE ========================")