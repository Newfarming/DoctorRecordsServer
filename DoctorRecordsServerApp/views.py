import time

from django.shortcuts import render

# Create your views here.
import json
import time
# import simplejson
from datetime import datetime, timedelta
from django.shortcuts import render, HttpResponse
from django.views import View
from util.doctorRecords_db import insertUser, editUser, deleteUser, userList, insertDepart, editDepart, deleteDepart, \
    departList, userInfo, departInfo, insertNewTechAward, insertNewTechResearch, insertResearchAward, \
    insertResearchProject, \
    insertOutTable, insertStudyTable, insertObtainPatents, insertResearchPapers, insertProfessionalTitle, \
    newTechAwardList, \
    newTechResearchList, outTableList, obtainPatentsList, professionalTitleList, researchProjectList, researchAwardList, \
    researchPapersList, studyTableList, doctorRelationshipDelete
from django.core import serializers
from django.http import JsonResponse
import jwt
from rest_framework.viewsets import GenericViewSet


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
        rst['prescription_normal'] = rst_term["prescription_normal"] == '1'
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
                                                                       "prescription_Corticosteroids_Short_glucocorticoid"] == '1'
    # 皮质激素类药物-冲击疗法-长疗程使用糖皮质激素
    if "prescription_Corticosteroids_Long_glucocorticoid" in rst_term:
        rst['prescription_Corticosteroids_Long_glucocorticoid'] = rst_term[
                                                                      "prescription_Corticosteroids_Long_glucocorticoid"] == '1'
    # 生物与血液制剂
    if "prescription_Biological_and_blood_preparations" in rst_term:
        rst['prescription_Biological_and_blood_preparations'] = rst_term[
                                                                    "prescription_Biological_and_blood_preparations"] == '1'
    if "depart_id" in rst_term:
        rst['depart_id'] = rst_term["depart_id"]
    if "id" in rst_term:
        rst['id'] = int(rst_term["id"])
    if "NewTechAwardList" in rst_term:
        rst['NewTechAwardList'] = rst_term["NewTechAwardList"]
    if "NewTechResearchList" in rst_term:
        rst['NewTechResearchList'] = rst_term["NewTechResearchList"]
    if "OutTableList" in rst_term:
        rst['OutTableList'] = rst_term["OutTableList"]
    if "ObtainPatentsList" in rst_term:
        rst['ObtainPatentsList'] = rst_term["ObtainPatentsList"]
    if "ProfessionalTitleList" in rst_term:
        rst['ProfessionalTitleList'] = rst_term["ProfessionalTitleList"]
    if "ResearchProjectList" in rst_term:
        rst['ResearchProjectList'] = rst_term["ResearchProjectList"]
    if "ResearchAwardList" in rst_term:
        rst['ResearchAwardList'] = rst_term["ResearchAwardList"]
    if "ResearchPapersList" in rst_term:
        rst['ResearchPapersList'] = rst_term["ResearchPapersList"]
    if "StudyTableList" in rst_term:
        rst['StudyTableList'] = rst_term["StudyTableList"]
    # if request.POST.get("password"):
    #     rst['password'] = request.POST.get("password")
    # if request.POST.get("permission_id"):
    #     rst['permission_id'] = request.POST.get("permission_id")
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
    decode_token = jwt.decode(token, "secret", algorithms=["HS256"])
    decode_depart = departInfo({'id': decode_token['id']})
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
        depart_obj = departInfo(get_obj)
        data_dict = {
            'username': depart_obj.title,
            'id': depart_obj.id
        }
        encoded_token = jwt.encode(data_dict, "secret", algorithm="HS256")
        return_obj = {
            'token': encoded_token,
            # 'token': '123456',
            # 'superAdmin': user_obj.superAdmin,
            # 'permission_name': user_obj.permission.name,
            'permission_type': depart_obj.permission_type,

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


class UserList(View):
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
        # data_array = json.loads(serializers.serialize("json", userList(rst)))
        depart_obj = token_get(request)
        if int(depart_obj.permission_type) == 2:
            typerst['search_type'] = 'depart__id'
            typerst['search'] = depart_obj.id
        user_set = userList(rst, typerst)
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


class UserAdd(View):
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
        doctor_obj = insertUser(rst_doctor)
        doctor_id = doctor_obj.id
        print('doctor_id:')
        print(doctor_id)
        print('NewTechAwardList')
        print(request.POST.get("NewTechAwardList"))
        if "ProfessionalTitleList" in rst:
            for item in rst["ProfessionalTitleList"]:
                item['doctor_id'] = doctor_id
                insertProfessionalTitle(item)
        if "StudyTableList" in rst:
            for item in rst["StudyTableList"]:
                item['doctor_id'] = doctor_id
                insertStudyTable(item)
        if "OutTableList" in rst:
            # OutTable = json.loads(request.POST.get("OutTableList"))
            for item in rst["OutTableList"]:
                item['doctor_id'] = doctor_id
                insertOutTable(item)
        if "ResearchProjectList" in rst:
            # ResearchProject = json.loads(request.POST.get("ResearchProjectList"))
            for item in rst["ResearchProjectList"]:
                item['doctor_id'] = doctor_id
                insertResearchProject(item)
        if "ResearchAwardList" in rst:
            # ResearchAward = json.loads(request.POST.get("ResearchAwardList"))
            for item in rst["ResearchAwardList"]:
                item['doctor_id'] = doctor_id
                insertResearchAward(item)
        if "ResearchPapersList" in rst:
            # ResearchPapers = json.loads(request.POST.get("ResearchPapersList"))
            for item in rst["ResearchPapersList"]:
                item['doctor_id'] = doctor_id
                insertResearchPapers(item)
        if "ObtainPatentsList" in rst:
            # ObtainPatents = json.loads(request.POST.get("ObtainPatentsList"))
            for item in rst["ObtainPatentsList"]:
                item['doctor_id'] = doctor_id
                insertObtainPatents(item)
        if "NewTechResearchList" in rst:
            # NewTechResearch = json.loads(request.POST.get("NewTechResearchList"))
            for item in rst["NewTechResearchList"]:
                item['doctor_id'] = doctor_id
                insertNewTechResearch(item)
        if "NewTechAwardList" in rst:
            for item in rst["NewTechAwardList"]:
                item['doctor_id'] = doctor_id
                insertNewTechAward(item)
        return JsonResponse({
            'message': 'success',
            'code': 20000,
            'data': 'success'
        }, safe=False)


def deleteRelete(doctor_id):
    doctorRelationshipDelete(doctor_id)


class UserEdit(View):
    def get(self, request):
        return HttpResponse('get UserEdit')

    def post(self, request):
        # data = json.loads(request.body.decode('utf-8'))
        rst = query_userinfo(request)
        rst_doctor = query_doctorinfo(request)
        # doctor_obj = userInfo(doctor_id)
        depart_obj = token_get(request)
        if int(depart_obj.permission_type) != 1 and depart_obj.id != int(rst_doctor['depart_id']):
            return JsonResponse({
                'message': 'fail',
                'code': 20000,
                'data': '你没有该操作权限'
            }, safe=False)
        doctor_id = int(rst['id'])
        print('doctor_id')
        print(doctor_id)
        deleteRelete({"doctor_id": doctor_id})
        editUser(doctor_id, rst_doctor)
        if "ProfessionalTitleList" in rst:
            for item in rst["ProfessionalTitleList"]:
                if "doctor" in item:
                    del item['doctor']
                item['doctor_id'] = doctor_id
                print(str(item))
                insertProfessionalTitle(item)
        if "StudyTableList" in rst:
            for item in rst["StudyTableList"]:
                if "doctor" in item:
                    del item['doctor']
                item['doctor_id'] = doctor_id
                insertStudyTable(item)
        if "OutTableList" in rst:
            # OutTable = json.loads(request.POST.get("OutTableList"))
            for item in rst["OutTableList"]:
                if "doctor" in item:
                    del item['doctor']
                item['doctor_id'] = doctor_id
                insertOutTable(item)
        if "ResearchProjectList" in rst:
            # ResearchProject = json.loads(request.POST.get("ResearchProjectList"))
            for item in rst["ResearchProjectList"]:
                if "doctor" in item:
                    del item['doctor']
                item['doctor_id'] = doctor_id
                insertResearchProject(item)
        if "ResearchAwardList" in rst:
            # ResearchAward = json.loads(request.POST.get("ResearchAwardList"))
            for item in rst["ResearchAwardList"]:
                if "doctor" in item:
                    del item['doctor']
                item['doctor_id'] = doctor_id
                insertResearchAward(item)
        if "ResearchPapersList" in rst:
            # ResearchPapers = json.loads(request.POST.get("ResearchPapersList"))
            for item in rst["ResearchPapersList"]:
                if "doctor" in item:
                    del item['doctor']
                item['doctor_id'] = doctor_id
                insertResearchPapers(item)
        if "ObtainPatentsList" in rst:
            # ObtainPatents = json.loads(request.POST.get("ObtainPatentsList"))
            for item in rst["ObtainPatentsList"]:
                if "doctor" in item:
                    del item['doctor']
                item['doctor_id'] = doctor_id
                insertObtainPatents(item)
        if "NewTechResearchList" in rst:
            # NewTechResearch = json.loads(request.POST.get("NewTechResearchList"))
            for item in rst["NewTechResearchList"]:
                if "doctor" in item:
                    del item['doctor']
                item['doctor_id'] = doctor_id
                insertNewTechResearch(item)
        if "NewTechAwardList" in rst:
            for item in rst["NewTechAwardList"]:
                if "doctor" in item:
                    del item['doctor']
                item['doctor_id'] = doctor_id
                insertNewTechAward(item)
        return JsonResponse({
            'message': 'success',
            'code': 20000,
            'data': 'success'
        }, safe=False)


class UserDelete(View):
    def get(self, request):
        return HttpResponse('get UserDelete')

    def post(self, request):
        # data = json.loads(request.body.decode('utf-8'))
        uid = request.POST.get("id")
        user_obj = userInfo({
            'id': request.GET.get('id'),
        })
        depart_obj = token_get(request)
        if int(depart_obj.permission_type) != 1 and depart_obj.id != int(user_obj.depart_id):
            return JsonResponse({
                'message': 'fail',
                'code': 20000,
                'data': '你没有该操作权限'
            }, safe=False)
        deleteUser(uid)
        return JsonResponse({
            'message': 'success',
            'code': 20000,
            'data': 'success'
        }, safe=False)


def database_to_list(arr):
    return_arr = []
    for item in arr:
        return_arr.append(item['fields'])
    return return_arr


def depart_to_srtlist(arr):
    return_arr = []
    for item in arr:
        return_arr.append({'id': item['pk'], 'title': item['fields']['title'], 'account': item['fields']['account'],
                           'password': item['fields']['password'],
                           'permission_type': item['fields']['permission_type']})
    return return_arr


def depart_to_open(arr):
    return_arr = []
    for item in arr:
        return_arr.append({'id': item.pk, 'title': item.fields.title})
    return return_arr


class UserDetails(View):
    def post(self, request):
        return HttpResponse('post UserDetails')

    def get(self, request):
        get_obj = {
            'id': request.GET.get('id'),
        }
        user_obj = userInfo(get_obj)
        depart_obj = token_get(request)
        if int(depart_obj.permission_type) != 1 and depart_obj.id != int(user_obj.depart_id):
            return JsonResponse({
                'message': 'fail',
                'code': 20000,
                'data': '你没有该操作权限'
            }, safe=False)
        rst = {
            "doctor_id": request.GET.get('id'),
        }
        return JsonResponse({
            'message': 'success',
            'code': 20000,
            'data': {
                'id': user_obj.id,
                'name': user_obj.name,
                'sex': user_obj.sex,
                'education': user_obj.education,
                'academic_degree': user_obj.academic_degree,
                'major': user_obj.major,
                'graduated_school': user_obj.graduated_school,
                'working_time': user_obj.working_time,
                'phone': user_obj.phone,
                'birthday': user_obj.birthday,
                'surgical_qualification_1': user_obj.surgical_qualification_1,
                'surgical_qualification_2': user_obj.surgical_qualification_2,
                'surgical_qualification_3': user_obj.surgical_qualification_3,
                'surgical_qualification_4': user_obj.surgical_qualification_4,
                'surgical_qualification_certificate_pic': user_obj.surgical_qualification_certificate_pic,
                'prescription_normal': user_obj.prescription_normal,
                'prescription_Antibacterials_restricted': user_obj.prescription_Antibacterials_restricted,
                'prescription_Antibacterials_unrestricted': user_obj.prescription_Antibacterials_unrestricted,
                'prescription_Antibacterials_special': user_obj.prescription_Antibacterials_special,
                'prescription_Antineoplastic_normal': user_obj.prescription_Antineoplastic_normal,
                'prescription_Antineoplastic_limited': user_obj.prescription_Antineoplastic_limited,
                'prescription_Narcotics_Narcotic_drugs': user_obj.prescription_Narcotics_Narcotic_drugs,
                'prescription_Narcotics_Psychotropic_first': user_obj.prescription_Narcotics_Psychotropic_first,
                'prescription_Narcotics_Psychotropic_second': user_obj.prescription_Narcotics_Psychotropic_second,
                'prescription_Corticosteroids_Short_glucocorticoid': user_obj.prescription_Corticosteroids_Short_glucocorticoid,
                'prescription_Corticosteroids_Long_glucocorticoid': user_obj.prescription_Corticosteroids_Long_glucocorticoid,
                'prescription_Biological_and_blood_preparations': user_obj.prescription_Biological_and_blood_preparations,
                'depart_id': user_obj.depart.id,
                'depart_name': user_obj.depart.title,
                'NewTechAwardList': database_to_list(json.loads(serializers.serialize("json", newTechAwardList(rst)))),
                'NewTechResearchList': database_to_list(
                    json.loads(serializers.serialize("json", newTechResearchList(rst)))),
                'OutTableList': database_to_list(json.loads(serializers.serialize("json", outTableList(rst)))),
                'ObtainPatentsList': database_to_list(
                    json.loads(serializers.serialize("json", obtainPatentsList(rst)))),
                'ProfessionalTitleList': database_to_list(
                    json.loads(serializers.serialize("json", professionalTitleList(rst)))),
                'ResearchProjectList': database_to_list(
                    json.loads(serializers.serialize("json", researchProjectList(rst)))),
                'ResearchAwardList': database_to_list(
                    json.loads(serializers.serialize("json", researchAwardList(rst)))),
                'ResearchPapersList': database_to_list(
                    json.loads(serializers.serialize("json", researchPapersList(rst)))),
                'StudyTableList': database_to_list(json.loads(serializers.serialize("json", studyTableList(rst)))),
            }
        }, safe=False)


class DepartAdd(View):
    def get(self, request):
        return HttpResponse('get DepartAdd')

    def post(self, request):
        # data = json.loads(request.body.decode('utf-8'))
        # rst = {'title': request.POST.get('title')}
        depart_obj = token_get(request)
        if int(depart_obj.permission_type) != 1:
            return JsonResponse({
                'message': 'fail',
                'code': 20000,
                'data': '你没有该操作权限'
            }, safe=False)
        rst_term = json.loads(request.body.decode())
        insertDepart({
            'title': rst_term['title'],
            'account': rst_term['account'],
            'password': rst_term['password'],
            'permission_type': '2'
        })
        return JsonResponse({
            'message': 'success',
            'code': 20000,
            'data': 'success'
        }, safe=False)


class DepartEdit(View):
    def get(self, request):
        return HttpResponse('get DepartEdit')

    def post(self, request):
        # data = json.loads(request.body.decode('utf-8'))
        depart_obj = token_get(request)
        if int(depart_obj.permission_type) != 1:
            return JsonResponse({
                'message': 'fail',
                'code': 20000,
                'data': '你没有该操作权限'
            }, safe=False)
        rst = {'title': request.POST.get('title')}
        nid = request.POST.get("id")
        editDepart(nid, rst)
        return JsonResponse({
            'message': 'success',
            'code': 20000,
            'data': 'success'
        }, safe=False)


class DepartDelete(View):
    def get(self, request):
        return HttpResponse('get DepartDelete')

    def post(self, request):
        # data = json.loads(request.body.decode('utf-8'))
        depart_obj = token_get(request)
        if int(depart_obj.permission_type) != 1:
            return JsonResponse({
                'message': 'fail',
                'code': 20000,
                'data': '你没有该操作权限'
            }, safe=False)
        nid = request.POST.get("id")
        deleteDepart(nid)
        return JsonResponse({
            'message': 'success',
            'code': 20000,
            'data': 'success'
        }, safe=False)


class DepartOpenList(View):
    def get(self, request):
        return HttpResponse('get UserList')

    def post(self, request):
        rst = {}
        if request.POST.get('search'):
            rst['search'] = request.POST.get('search')
            rst['search_type'] = 'title'
        if request.POST.get('pageStart'):
            rst['pageStart'] = request.POST.get('pageStart')
        if request.POST.get('pagesize'):
            rst['pagesize'] = request.POST.get('pagesize')
        data_dict = depart_to_open(json.loads(serializers.serialize("json", departList(rst))))
        return JsonResponse({
            'message': 'success',
            'code': 20000,
            'data': data_dict
        }, safe=False)


class DepartList(View):
    def post(self, request):
        return HttpResponse('post UserList')

    def get(self, request):
        rst = {}
        depart_obj = token_get(request)
        if request.GET.get('search'):
            rst['search'] = request.GET.get('search')
            rst['search_type'] = 'title'
        if request.GET.get('pageStart'):
            rst['pageStart'] = request.GET.get('pageStart')
        if request.GET.get('pagesize'):
            rst['pagesize'] = request.GET.get('pagesize')
        if int(depart_obj.permission_type) == 2:
            rst['search_type'] = 'id'
            rst['search'] = depart_obj.id
        # data_dict = database_to_list(json.loads(serializers.serialize("json", departList(rst))))
        data_dict = depart_to_srtlist(json.loads(serializers.serialize("json", departList(rst))))
        return JsonResponse({
            'message': 'success',
            'code': 20000,
            'data': data_dict
        }, safe=False)


class DepartDetails(View):
    def post(self, request):
        return HttpResponse('post DepatyDetails')

    def get(self, request):
        get_obj = {
            'id': request.GET.get('id')
        }
        depart_obj = token_get(request)
        if int(depart_obj.permission_type) != 1:
            return JsonResponse({
                'message': 'fail',
                'code': 20000,
                'data': '你没有该操作权限'
            }, safe=False)
        depart_obj = departInfo(get_obj)
        return JsonResponse({
            'message': 'success',
            'code': 20000,
            'data': {
                'title': depart_obj.title,
                'id': depart_obj.id,
                'account': depart_obj.account,
                'password': depart_obj.password
            }
        }, safe=False)


class UploadImg(View):
    # 保存图片
    def get(self, request):
        return HttpResponse('get DepatyDetails')

    def post(post, request):
        print('FILES')
        print(str(request.FILES))

        current_milli_time = int(round(time.time() * 1000))
        print('current_milli_time')
        print(str(current_milli_time))
        file = request.FILES.get('file')
        try:
            # 构造图片保存路径
            file.name = str(current_milli_time) + file.name
            print('file.name')
            print(file.name)
            file_path = './DoctorRecordsServerApp/media/img/' + file.name
            # 保存图片
            with open(file_path, 'wb+') as f:
                f.write(file.read())
                f.close()
            response = {
                'message': 'success',
                'code': 20000,
                'data': {
                    'imgurl': '/DoctorRecordsServerApp/media/img/' + file.name,
                }
            }
        except:
            response = {'date': '', 'code': 201, 'message': "fail"}
        return JsonResponse(response, safe=False)


class HomePage(View):
    def get(self, request):
        return render(request, 'index.html')
