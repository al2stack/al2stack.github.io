# # with open("weather_data.csv") as raw_list:
# #     data=raw_list.readlines()
# # import csv
# # with open("weather_data.csv") as data_file:
# #     data=csv.reader(data_file)
# #     temperatures=[]
# #     for row in data:
# #         if row[1]!="temp":
# #            temperatures.append(int(row[1]))
# #     print(temperatures)
# import pandas
# data = pandas.read_csv("weather_data.csv")
# # print(data["temp"])
# # data_dict=data.to_dict()
# # print(data_dict)
# # avg_temp=data["temp"].mean()
# # print(avg_temp)
# # max_val=data["temp"].max()
# # print(max_val)
#
# #get data in row
# # print(data[data.day == "Monday"])
# # print(data[data.temp == data.temp.max()])
#
# monday=data[data.day == "Monday"]
# f_temp=monday.temp*1.8 + 32
# print(f_temp)
#
# #create a data frame
import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_num = len(data[data["Primary Fur Color"] == "Gray"])
red_num=len(data[data["Primary Fur Color"] == "Black"])
cinammon_num=len(data[data["Primary Fur Color"] == "Cinnamon"])
color_list=[gray_num,red_num,cinammon_num]
dict={
    "Fur Color":["Gray","Black","Cinnamon"],
    "Count":color_list
}
new_frame=pandas.DataFrame(dict)
new_frame.to_csv("new_list.csv")