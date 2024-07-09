from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

# Create your views here.
import json
import time
# import simplejson
from datetime import datetime, timedelta
from django.shortcuts import render, HttpResponse
from django.views import View
from util.MedInsNoPaper_db import MedInsInfo, userInfo, MedInsList, insertMedIns
from django.http import JsonResponse
import jwt


def query_userinfo(request):
    rst = {}
    rst_term = json.loads(request.body.decode())
    # 姓名
    if "name" in rst_term:
        rst['name'] = rst_term["name"]
    # 性别
    if "sex" in rst_term:
        rst['sex'] = rst_term["sex"]
    # 学历
    if "education" in rst_term:
        rst['education'] = rst_term["education"]
    # 学位
    if "academic_degree" in rst_term:
        rst['academic_degree'] = rst_term["academic_degree"]
    # 专业
    if "major" in rst_term:
        rst['major'] = rst_term["major"]
    # 毕业院校
    if "graduated_school" in rst_term:
        rst['graduated_school'] = rst_term["graduated_school"]
    # 参加工作时间
    if "working_time" in rst_term:
        rst['working_time'] = rst_term["working_time"]
    # 联系电话
    if "phone" in rst_term:
        rst['phone'] = rst_term["phone"]
    # 生日
    return rst


def query_doctorinfo(request):
    rst = {}
    rst_term = json.loads(request.body.decode())
    # 姓名
    if "name" in rst_term:
        rst['name'] = rst_term["name"]
    # 性别
    if "sex" in rst_term:
        rst['sex'] = rst_term["sex"]
    # 学历
    if "education" in rst_term:
        rst['education'] = rst_term["education"]
    # 学位
    if "academic_degree" in rst_term:
        rst['academic_degree'] = rst_term["academic_degree"]
    # 专业
    if "major" in rst_term:
        rst['major'] = rst_term["major"]
    # 毕业院校
    if "graduated_school" in rst_term:
        rst['graduated_school'] = rst_term["graduated_school"]
    # 参加工作时间
    if "working_time" in rst_term:
        rst['working_time'] = rst_term["working_time"]
    # 联系电话
    if "phone" in rst_term:
        rst['phone'] = rst_term["phone"]
    # 生日
    if "birthday" in rst_term:
        rst['birthday'] = rst_term["birthday"]
    # 手术资质1
    if "surgical_qualification_1" in rst_term:
        rst['surgical_qualification_1'] = rst_term["surgical_qualification_1"]
    # 手术资质2
    if "surgical_qualification_2" in rst_term:
        rst['surgical_qualification_2'] = rst_term["surgical_qualification_2"]
    # 手术资质3
    if "surgical_qualification_3" in rst_term:
        rst['surgical_qualification_3'] = rst_term["surgical_qualification_3"]
    # 手术资质4
    if "surgical_qualification_4" in rst_term:
        rst['surgical_qualification_4'] = rst_term["surgical_qualification_4"]
    # 手术资质授权表
    if "surgical_qualification_certificate_pic" in rst_term:
        rst['surgical_qualification_certificate_pic'] = rst_term["surgical_qualification_certificate_pic"]
    # 普通处方权
    if "prescription_normal" in rst_term:
        rst['prescription_normal'] = rst_term["prescription_normal"]
    # 抗菌药物-限制级
    if "prescription_Antibacterials_restricted" in rst_term:
        rst['prescription_Antibacterials_restricted'] = rst_term["prescription_Antibacterials_restricted"]
    # 抗菌药物-非限制级
    if "prescription_Antibacterials_unrestricted" in rst_term:
        rst['prescription_Antibacterials_unrestricted'] = rst_term["prescription_Antibacterials_unrestricted"]
    # 抗菌药物-特殊级
    if "prescription_Antibacterials_special" in rst_term:
        rst['prescription_Antibacterials_special'] = rst_term["prescription_Antibacterials_special"]
    # 抗肿瘤药物普通
    if "prescription_Antineoplastic_normal" in rst_term:
        rst['prescription_Antineoplastic_normal'] = rst_term["prescription_Antineoplastic_normal"]
    # 抗肿瘤药物限制
    if "prescription_Antineoplastic_limited" in rst_term:
        rst['prescription_Antineoplastic_limited'] = rst_term["prescription_Antineoplastic_limited"]
    # 麻醉精神类-麻醉药品
    if "prescription_Narcotics_Narcotic_drugs" in rst_term:
        rst['prescription_Narcotics_Narcotic_drugs'] = rst_term["prescription_Narcotics_Narcotic_drugs"]
    # 麻醉精神类-第一类精神药品
    if "prescription_Narcotics_Psychotropic_first" in rst_term:
        rst['prescription_Narcotics_Psychotropic_first'] = rst_term["prescription_Narcotics_Psychotropic_first"]
    # 麻醉精神类-第二类精神药品
    if "prescription_Narcotics_Psychotropic_second" in rst_term:
        rst['prescription_Narcotics_Psychotropic_second'] = rst_term["prescription_Narcotics_Psychotropic_second"]
    # 皮质激素类药物-短中程使用糖皮质激素
    if "prescription_Corticosteroids_Short_glucocorticoid" in rst_term:
        rst['prescription_Corticosteroids_Short_glucocorticoid'] = rst_term[
            "prescription_Corticosteroids_Short_glucocorticoid"]
    # 皮质激素类药物-冲击疗法-长疗程使用糖皮质激素
    if "prescription_Corticosteroids_Long_glucocorticoid" in rst_term:
        rst['prescription_Corticosteroids_Long_glucocorticoid'] = rst_term[
            "prescription_Corticosteroids_Long_glucocorticoid"]
    # 生物与血液制剂
    if "prescription_Biological_and_blood_preparations" in rst_term:
        rst['prescription_Biological_and_blood_preparations'] = rst_term[
            "prescription_Biological_and_blood_preparations"]
    # 肠外营养制剂
    if "changwaiyingyangzhiji" in rst_term:
        rst['changwaiyingyangzhiji'] = rst_term["changwaiyingyangzhiji"]
    # 急诊用血
    if "jizhenyongxue" in rst_term:
        rst['jizhenyongxue'] = rst_term["jizhenyongxue"]
    # 平诊用血
    if "pingzhenyongxue" in rst_term:
        rst['pingzhenyongxue'] = rst_term["pingzhenyongxue"]
    # 用血量小于800
    if "yongxueliangxiaoyu800" in rst_term:
        rst['yongxueliangxiaoyu800'] = rst_term["yongxueliangxiaoyu800"]
    # 用血量小于1600
    if "yongxueliangxiaoyu1600" in rst_term:
        rst['yongxueliangxiaoyu1600'] = rst_term["yongxueliangxiaoyu1600"]
    # 检验报告
    if "jianyanbaogao" in rst_term:
        rst['jianyanbaogao'] = rst_term["jianyanbaogao"]
    # 检查报告
    if "jianchabaogao" in rst_term:
        rst['jianchabaogao'] = rst_term["jianchabaogao"]
    # 输血检验报告
    if "shuxuejianyanbaogao" in rst_term:
        rst['shuxuejianyanbaogao'] = rst_term["shuxuejianyanbaogao"]

    if "depart_id" in rst_term:
        rst['depart_id'] = rst_term["depart_id"]
    # if "id" in rst_term:
    #     print('query_doctorinfo id')
    #     print(rst_term['id'])
    #     rst['id'] = int(rst_term["id"])
    return rst


def token_get(request):
    token = request.META.get('HTTP_TOKEN')
    # print('token')
    # print(token)
    # encoded_token = jwt.encode(data_dict, "secret", algorithm="HS256")
    decode_token = jwt.decode(token, "secret_code_lfm", algorithms=["HS256"])
    decode_depart = MedInsInfo({'id': decode_token['id']})
    print('decode_depart')
    print(str(decode_depart))
    return decode_depart


class UserLogin(View):
    def post(self, request):
        return HttpResponse('post login')

    def get(self, request):
        print(' get message')
        get_obj = {
            'account': request.GET.get('username'),
            'password': request.GET.get('password')
        }
        medins_obj = userInfo(get_obj)
        print('medins_obj')
        print(medins_obj)
        data_dict = {
            'username': medins_obj.account,
            'id': medins_obj.id
        }
        encoded_token = jwt.encode(data_dict, "secret_code_lfm", algorithm="HS256")
        return_obj = {
            'token': encoded_token,
            # 'token': '123456',
            # 'superAdmin': user_obj.superAdmin,
            # 'permission_name': user_obj.permission.name,
            'permission_type': medins_obj.permission_type,
            'user_id': medins_obj.id

        }
        if True:
            print('have user_obj')
            return_data = {
                'message': 'success',
                'code': 20000,
                'data': return_obj
            }
            return JsonResponse(return_data)
        else:
            return_data = {
                'message': 'fail',
                'code': 100,
                'data': return_obj
            }
            print('no user_obj')
            return JsonResponse(return_data, safe=False)


class User_Info(View):
    def post(self, request):
        return HttpResponse('post User_Info')

    def get(self, request):
        token = request.POST.get('token')
        # decode_token = jwt.decode(token, "secret", algorithms=["HS256"])
        # get_obj = {
        #     'id': decode_token['id'],
        # }
        # user_obj = userInfo(get_obj)
        data_dict = {
            'roles': ['admin'],
            'introduction': '',
            'avatar': 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif',
            'name': 'user_obj.name',
            'permission_name': 'type',
            'permission_type': '1,2,3,4,5,6,7,8,9,10,11,12',
        }
        return JsonResponse({
            'message': 'success',
            'code': 20000,
            'data': data_dict
        }, safe=False)


class MedInsList(View):
    def post(self, request):
        return HttpResponse('post Userlist')

    def get(self, request):
        rst = {}
        typerst = {}
        print('request')
        print(request.GET)
        if request.GET.get('search'):
            rst['search'] = request.GET['search']
        if request.GET.get('search_type'):
            rst['search_type'] = request.GET['search_type']
        if request.GET.get('pageStart'):
            rst['pageStart'] = request.GET['pageStart']
        if request.GET.get('pagesize'):
            rst['pagesize'] = request.GET['pagesize']
        if request.GET.get('depart_id'):
            typerst['search_type'] = 'depart__id'
            typerst['search'] = int(request.GET.get('depart_id'))
        # data_array = json.loads(serializers.serialize("json", userList(rst)))
        depart_obj = token_get(request)
        if int(depart_obj.permission_type) == 2:
            typerst['search_type'] = 'depart__id'
            typerst['search'] = depart_obj.id
        user_set = MedInsList(rst, typerst)
        userlist_set = user_set[
            slice(int(rst['pageStart']) * int(rst['pagesize']), (int(rst['pageStart']) + 1) * int(rst['pagesize']))]
        return_arr = []
        # dataLength =len(userlist_set)
        for index in range(len(userlist_set)):
            # print(index, data_array[index]['pk'])
            return_arr.append({
                'id': userlist_set[index].pk,
                'name': userlist_set[index].name,
                'sex': userlist_set[index].sex,
                'phone': userlist_set[index].phone,
                'depart_id': userlist_set[index].depart.id,
                'depart_name': userlist_set[index].depart.title,
            })

        return JsonResponse({
            'message': 'success',
            'code': 20000,
            'data': return_arr,
            'total': len(user_set)
        }, safe=False)


class MedInsAdd(View):
    def get(self, request):
        return HttpResponse('get UserAdd')

    def post(self, request):
        # data = json.loads(request.body.decode('utf-8'))
        rst = query_userinfo(request)
        rst_doctor = query_doctorinfo(request)
        depart_obj = token_get(request)
        if int(depart_obj.permission_type) != 1 and depart_obj.id != int(rst_doctor['depart_id']):
            return JsonResponse({
                'message': 'fail',
                'code': 20000,
                'data': '你没有该操作权限'
            }, safe=False)
        doctor_obj = insertMedIns(rst_doctor)
        doctor_id = doctor_obj.id
        print('doctor_id:')
        print(doctor_id)
        print('NewTechAwardList')
        print(request.POST.get("NewTechAwardList"))
        return JsonResponse({
            'message': 'success',
            'code': 20000,
            'data': 'success'
        }, safe=False)


# class MedInsEdit(View):
#     def get(self, request):
#         return HttpResponse('get UserEdit')
#
#     def post(self, request):
#         # data = json.loads(request.body.decode('utf-8'))
#         rst = query_userinfo(request)
#         rst_doctor = query_doctorinfo(request)
#         # doctor_obj = userInfo(doctor_id)
#         depart_obj = token_get(request)
#         if int(depart_obj.permission_type) != 1 and depart_obj.id != int(rst_doctor['depart_id']):
#             return JsonResponse({
#                 'message': 'fail',
#                 'code': 20000,
#                 'data': '你没有该操作权限'
#             }, safe=False)
#         doctor_id = int(rst['id'])
#         print('doctor_id')
#         print(doctor_id)
#         deleteRelete({"doctor_id": doctor_id})
#         editUser(doctor_id, rst_doctor)
#         if "ProfessionalTitleList" in rst:
#             for item in rst["ProfessionalTitleList"]:
#                 if "doctor" in item:
#                     del item['doctor']
#                 item['doctor_id'] = doctor_id
#                 print(str(item))
#                 insertProfessionalTitle(item)
#         if "StudyTableList" in rst:
#             for item in rst["StudyTableList"]:
#                 if "doctor" in item:
#                     del item['doctor']
#                 item['doctor_id'] = doctor_id
#                 insertStudyTable(item)
#         if "OutTableList" in rst:
#             # OutTable = json.loads(request.POST.get("OutTableList"))
#             for item in rst["OutTableList"]:
#                 if "doctor" in item:
#                     del item['doctor']
#                 item['doctor_id'] = doctor_id
#                 insertOutTable(item)
#         if "ResearchProjectList" in rst:
#             # ResearchProject = json.loads(request.POST.get("ResearchProjectList"))
#             for item in rst["ResearchProjectList"]:
#                 if "doctor" in item:
#                     del item['doctor']
#                 item['doctor_id'] = doctor_id
#                 insertResearchProject(item)
#         if "ResearchAwardList" in rst:
#             # ResearchAward = json.loads(request.POST.get("ResearchAwardList"))
#             for item in rst["ResearchAwardList"]:
#                 if "doctor" in item:
#                     del item['doctor']
#                 item['doctor_id'] = doctor_id
#                 insertResearchAward(item)
#         if "ResearchPapersList" in rst:
#             # ResearchPapers = json.loads(request.POST.get("ResearchPapersList"))
#             for item in rst["ResearchPapersList"]:
#                 if "doctor" in item:
#                     del item['doctor']
#                 item['doctor_id'] = doctor_id
#                 insertResearchPapers(item)
#         if "ObtainPatentsList" in rst:
#             # ObtainPatents = json.loads(request.POST.get("ObtainPatentsList"))
#             for item in rst["ObtainPatentsList"]:
#                 if "doctor" in item:
#                     del item['doctor']
#                 item['doctor_id'] = doctor_id
#                 insertObtainPatents(item)
#         if "NewTechResearchList" in rst:
#             # NewTechResearch = json.loads(request.POST.get("NewTechResearchList"))
#             for item in rst["NewTechResearchList"]:
#                 if "doctor" in item:
#                     del item['doctor']
#                 item['doctor_id'] = doctor_id
#                 insertNewTechResearch(item)
#         if "NewTechAwardList" in rst:
#             for item in rst["NewTechAwardList"]:
#                 if "doctor" in item:
#                     del item['doctor']
#                 item['doctor_id'] = doctor_id
#                 insertNewTechAward(item)
#         if "shoushuzizhiList" in rst:
#             for item in rst["shoushuzizhiList"]:
#                 if "doctor" in item:
#                     del item['doctor']
#                 item['doctor_id'] = doctor_id
#                 insert_shoushuzizhi(item)
#         if "chufang_shengwuyuxueyezhijiList" in rst:
#             for item in rst["chufang_shengwuyuxueyezhijiList"]:
#                 if "doctor" in item:
#                     del item['doctor']
#                 item['doctor_id'] = doctor_id
#                 insert_chufang_shengwuyuxueyezhiji(item)
#         if "chufang_putongchufangquanList" in rst:
#             for item in rst["chufang_putongchufangquanList"]:
#                 if "doctor" in item:
#                     del item['doctor']
#                 item['doctor_id'] = doctor_id
#                 insert_chufang_putongchufangquan(item)
#         if "chufang_pizhijisuleiyaowuList" in rst:
#             for item in rst["chufang_pizhijisuleiyaowuList"]:
#                 if "doctor" in item:
#                     del item['doctor']
#                 item['doctor_id'] = doctor_id
#                 insert_chufang_pizhijisuleiyaowu(item)
#         if "chufang_baogaoqianziquanList" in rst:
#             for item in rst["chufang_baogaoqianziquanList"]:
#                 if "doctor" in item:
#                     del item['doctor']
#                 item['doctor_id'] = doctor_id
#                 insert_chufang_baogaoqianziquan(item)
#         if "chufang_yongxuezizhiList" in rst:
#             for item in rst["chufang_yongxuezizhiList"]:
#                 if "doctor" in item:
#                     del item['doctor']
#                 item['doctor_id'] = doctor_id
#                 insert_chufang_yongxuezizhi(item)
#         if "chufang_kangzhongliuList" in rst:
#             for item in rst["chufang_kangzhongliuList"]:
#                 if "doctor" in item:
#                     del item['doctor']
#                 item['doctor_id'] = doctor_id
#                 insert_chufang_kangzhongliu(item)
#         if "chufang_mazuijingshenList" in rst:
#             for item in rst["chufang_mazuijingshenList"]:
#                 if "doctor" in item:
#                     del item['doctor']
#                 item['doctor_id'] = doctor_id
#                 insert_chufang_mazuijingshen(item)
#         if "chufang_kangjunyaowuList" in rst:
#             for item in rst["chufang_kangjunyaowuList"]:
#                 if "doctor" in item:
#                     del item['doctor']
#                 item['doctor_id'] = doctor_id
#                 insert_chufang_kangjunyaowu(item)
#         if "chufang_changwaiyingyangzhijiList" in rst:
#             for item in rst["chufang_changwaiyingyangzhijiList"]:
#                 if "doctor" in item:
#                     del item['doctor']
#                 item['doctor_id'] = doctor_id
#                 insert_chufang_changwaiyingyangzhiji(item)
#         if "chufang_shouquanList" in rst:
#             for item in rst["chufang_shouquanList"]:
#                 if "doctor" in item:
#                     del item['doctor']
#                 item['doctor_id'] = doctor_id
#                 insert_chufang_shouquan(item)
#         return JsonResponse({
#             'message': 'success',
#             'code': 20000,
#             'data': 'success'
#         }, safe=False)
#
#
# class MedInsDelete(View):
#     def get(self, request):
#         return HttpResponse('get UserDelete')
#
#     def post(self, request):
#         # data = json.loads(request.body.decode('utf-8'))
#         rst_term = json.loads(request.body.decode())
#         if rst_term['id']:
#             uid = rst_term['id']
#         else:
#             return JsonResponse({
#                 'message': 'fail',
#                 'code': 20000,
#                 'data': '参数没有需要删除用户id'
#             }, safe=False)
#         user_obj = userInfo({
#             'id': uid,
#         })
#         depart_obj = token_get(request)
#         print('depart_obj.permission_type)')
#         print(depart_obj.permission_type)
#         print('depart_obj.id ')
#         print(depart_obj.id )
#         print('uid')
#         print(uid)
#         # print(user_obj.depart_id)
#         if int(depart_obj.permission_type) != 1 and depart_obj.id != int(user_obj.depart_id):
#             return JsonResponse({
#                 'message': 'fail',
#                 'code': 20000,
#                 'data': '你没有该操作权限'
#             }, safe=False)
#         deleteUser(uid)
#         return JsonResponse({
#             'message': 'success',
#             'code': 20000,
#             'data': 'success'
#         }, safe=False)
#
#
# class MedInsDetails(View):
#     def post(self, request):
#         return HttpResponse('post UserDetails')
#
#     def get(self, request):
#         get_obj = {
#             'id': request.GET.get('id'),
#         }
#         user_obj = userInfo(get_obj)
#         depart_obj = token_get(request)
#         if int(depart_obj.permission_type) != 1 and depart_obj.id != int(user_obj.depart_id):
#             return JsonResponse({
#                 'message': 'fail',
#                 'code': 20000,
#                 'data': '你没有该操作权限'
#             }, safe=False)
#         rst = {
#             "doctor_id": request.GET.get('id'),
#         }
#         return JsonResponse({
#             'message': 'success',
#             'code': 20000,
#             'data': {
#                 'id': user_obj.id,
#                 'name': user_obj.name,
#                 'sex': user_obj.sex,
#                 'education': user_obj.education,
#                 'academic_degree': user_obj.academic_degree,
#                 'major': user_obj.major,
#                 'graduated_school': user_obj.graduated_school,
#                 'working_time': user_obj.working_time,
#                 'phone': user_obj.phone,
#                 'birthday': user_obj.birthday,
#                 'surgical_qualification_1': user_obj.surgical_qualification_1,
#                 'surgical_qualification_2': user_obj.surgical_qualification_2,
#                 'surgical_qualification_3': user_obj.surgical_qualification_3,
#                 'surgical_qualification_4': user_obj.surgical_qualification_4,
#                 'surgical_qualification_certificate_pic': user_obj.surgical_qualification_certificate_pic,
#                 'prescription_normal': user_obj.prescription_normal,
#                 'prescription_Antibacterials_restricted': user_obj.prescription_Antibacterials_restricted,
#                 'prescription_Antibacterials_unrestricted': user_obj.prescription_Antibacterials_unrestricted,
#                 'prescription_Antibacterials_special': user_obj.prescription_Antibacterials_special,
#                 'prescription_Antineoplastic_normal': user_obj.prescription_Antineoplastic_normal,
#                 'prescription_Antineoplastic_limited': user_obj.prescription_Antineoplastic_limited,
#                 'prescription_Narcotics_Narcotic_drugs': user_obj.prescription_Narcotics_Narcotic_drugs,
#                 'prescription_Narcotics_Psychotropic_first': user_obj.prescription_Narcotics_Psychotropic_first,
#                 'prescription_Narcotics_Psychotropic_second': user_obj.prescription_Narcotics_Psychotropic_second,
#                 'prescription_Corticosteroids_Short_glucocorticoid': user_obj.prescription_Corticosteroids_Short_glucocorticoid,
#                 'prescription_Corticosteroids_Long_glucocorticoid': user_obj.prescription_Corticosteroids_Long_glucocorticoid,
#                 'prescription_Biological_and_blood_preparations': user_obj.prescription_Biological_and_blood_preparations,
#                 'changwaiyingyangzhiji': user_obj.changwaiyingyangzhiji,
#                 'jizhenyongxue': user_obj.jizhenyongxue,
#                 'pingzhenyongxue': user_obj.pingzhenyongxue,
#                 'yongxueliangxiaoyu800': user_obj.yongxueliangxiaoyu800,
#                 'yongxueliangxiaoyu1600': user_obj.yongxueliangxiaoyu1600,
#                 'jianyanbaogao': user_obj.jianyanbaogao,
#                 'jianchabaogao': user_obj.jianchabaogao,
#                 'shuxuejianyanbaogao': user_obj.shuxuejianyanbaogao,
#                 'depart_id': user_obj.depart.id,
#                 'depart_name': user_obj.depart.title,
#                 'NewTechAwardList': database_to_list(json.loads(serializers.serialize("json", newTechAwardList(rst)))),
#                 'NewTechResearchList': database_to_list(
#                     json.loads(serializers.serialize("json", newTechResearchList(rst)))),
#                 'OutTableList': database_to_list(json.loads(serializers.serialize("json", outTableList(rst)))),
#                 'ObtainPatentsList': database_to_list(
#                     json.loads(serializers.serialize("json", obtainPatentsList(rst)))),
#                 'ProfessionalTitleList': database_to_list(
#                     json.loads(serializers.serialize("json", professionalTitleList(rst)))),
#                 'ResearchProjectList': database_to_list(
#                     json.loads(serializers.serialize("json", researchProjectList(rst)))),
#                 'ResearchAwardList': database_to_list(
#                     json.loads(serializers.serialize("json", researchAwardList(rst)))),
#                 'ResearchPapersList': database_to_list(
#                     json.loads(serializers.serialize("json", researchPapersList(rst)))),
#                 'StudyTableList': database_to_list(json.loads(serializers.serialize("json", studyTableList(rst)))),
#                 'shoushuzizhiList': database_to_list(json.loads(serializers.serialize("json", list_shoushuzizhi(rst)))),
#                 'chufang_yongxuezizhiList': database_to_list(json.loads(serializers.serialize("json", list_chufang_yongxuezizhi(rst)))),
#                 'chufang_kangjunyaowuList': database_to_list(json.loads(serializers.serialize("json", list_chufang_kangjunyaowu(rst)))),
#                 'chufang_kangzhongliuList': database_to_list(json.loads(serializers.serialize("json", list_chufang_kangzhongliu(rst)))),
#                 'chufang_mazuijingshenList': database_to_list(json.loads(serializers.serialize("json", list_chufang_mazuijingshen(rst)))),
#                 'chufang_changwaiyingyangzhijiList': database_to_list(json.loads(serializers.serialize("json", list_chufang_changwaiyingyangzhiji(rst)))),
#                 'chufang_baogaoqianziquanList': database_to_list(json.loads(serializers.serialize("json", list_chufang_baogaoqianziquan(rst)))),
#                 'chufang_pizhijisuleiyaowuList': database_to_list(json.loads(serializers.serialize("json", list_chufang_pizhijisuleiyaowu(rst)))),
#                 'chufang_putongchufangquanList': database_to_list(json.loads(serializers.serialize("json", list_chufang_putongchufangquan(rst)))),
#                 'chufang_shengwuyuxueyezhijiList': database_to_list(json.loads(serializers.serialize("json", list_chufang_shengwuyuxueyezhiji(rst)))),
#                 'chufang_shouquanList': database_to_list(json.loads(serializers.serialize("json", list_chufang_shouquan(rst)))),
#             }
#         }, safe=False)
