import pymysql, json
from DoctorRecordsServerApp.models import DoctorInfo, Department, NewTechAward, NewTechResearch, OutTable, \
    ObtainPatents, ProfessionalTitle, ResearchProject, ResearchAward, ResearchPapers, StudyTable, shoushuzizhi, \
    chufang_yongxuezizhi, chufang_kangjunyaowu, chufang_kangzhongliu, chufang_mazuijingshen, \
    chufang_changwaiyingyangzhiji, \
    chufang_baogaoqianziquan, chufang_pizhijisuleiyaowu, chufang_putongchufangquan, chufang_shengwuyuxueyezhiji,\
    chufang_shouquan


def doctorRelationshipDelete(data_dict):
    NewTechAward.objects.filter(**data_dict).delete()
    NewTechResearch.objects.filter(**data_dict).delete()
    OutTable.objects.filter(**data_dict).delete()
    ObtainPatents.objects.filter(**data_dict).delete()
    ProfessionalTitle.objects.filter(**data_dict).delete()
    ResearchAward.objects.filter(**data_dict).delete()
    ResearchPapers.objects.filter(**data_dict).delete()
    ResearchProject.objects.filter(**data_dict).delete()
    StudyTable.objects.filter(**data_dict).delete()
    shoushuzizhi.objects.filter(**data_dict).delete()
    chufang_changwaiyingyangzhiji.objects.filter(**data_dict).delete()
    chufang_yongxuezizhi.objects.filter(**data_dict).delete()
    chufang_baogaoqianziquan.objects.filter(**data_dict).delete()
    chufang_kangjunyaowu.objects.filter(**data_dict).delete()
    chufang_pizhijisuleiyaowu.objects.filter(**data_dict).delete()
    chufang_mazuijingshen.objects.filter(**data_dict).delete()
    chufang_kangzhongliu.objects.filter(**data_dict).delete()
    chufang_putongchufangquan.objects.filter(**data_dict).delete()
    chufang_shengwuyuxueyezhiji.objects.filter(**data_dict).delete()
    chufang_shouquan.objects.filter(**data_dict).delete()

def studyTableInfo(data_dict):
    return StudyTable.objects.filter(**data_dict).first()


def insertStudyTable(data_dict):
    StudyTable.objects.create(**data_dict)


def deleteStudyTable(nid):
    StudyTable.objects.filter(id=nid).delete()


def editStudyTable(nid, data_dict):
    StudyTable.objects.filter(id=nid).update(**data_dict)


def studyTableList(data_dict):
    data_set = StudyTable.objects.filter(**data_dict)
    return data_set


def researchPapersInfo(data_dict):
    return ResearchPapers.objects.filter(**data_dict).first()


def insertResearchPapers(data_dict):
    ResearchPapers.objects.create(**data_dict)


def deleteResearchPapers(nid):
    ResearchPapers.objects.filter(id=nid).delete()


def editResearchPapers(nid, data_dict):
    ResearchPapers.objects.filter(id=nid).update(**data_dict)


def researchPapersList(data_dict):
    data_set = ResearchPapers.objects.filter(**data_dict)
    return data_set


def ResearchAwardInfo(data_dict):
    return ResearchProject.objects.filter(**data_dict).first()


def researchAwardInfo(data_dict):
    return ResearchAward.objects.filter(**data_dict).first()


def insertResearchAward(data_dict):
    ResearchAward.objects.create(**data_dict)


def deleteResearchAward(nid):
    ResearchAward.objects.filter(id=nid).delete()


def editResearchAward(nid, data_dict):
    ResearchAward.objects.filter(id=nid).update(**data_dict)


def researchAwardList(data_dict):
    data_set = ResearchAward.objects.filter(**data_dict)
    return data_set


def ResearchAwardInfo(data_dict):
    return ResearchProject.objects.filter(**data_dict).first()


def insertResearchProject(data_dict):
    ResearchProject.objects.create(**data_dict)


def deleteResearchProject(nid):
    ResearchProject.objects.filter(id=nid).delete()


def editResearchProject(nid, data_dict):
    ResearchProject.objects.filter(id=nid).update(**data_dict)


def researchProjectList(data_dict):
    data_set = ResearchProject.objects.filter(**data_dict)
    return data_set


def professionalTitleInfo(data_dict):
    return ProfessionalTitle.objects.filter(**data_dict).first()


def insertProfessionalTitle(data_dict):
    ProfessionalTitle.objects.create(**data_dict)


def deleteProfessionalTitle(nid):
    ProfessionalTitle.objects.filter(id=nid).delete()


def editProfessionalTitle(nid, data_dict):
    ProfessionalTitle.objects.filter(id=nid).update(**data_dict)


def professionalTitleList(data_dict):
    data_set = ProfessionalTitle.objects.filter(**data_dict)
    return data_set


def obtainPatentsInfo(data_dict):
    return ObtainPatents.objects.filter(**data_dict).first()


def insertObtainPatents(data_dict):
    ObtainPatents.objects.create(**data_dict)


def deleteObtainPatents(nid):
    ObtainPatents.objects.filter(id=nid).delete()


def editObtainPatents(nid, data_dict):
    ObtainPatents.objects.filter(id=nid).update(**data_dict)


def obtainPatentsList(data_dict):
    data_set = ObtainPatents.objects.filter(**data_dict)
    return data_set


def outTableInfo(data_dict):
    return OutTable.objects.filter(**data_dict).first()


def insertOutTable(data_dict):
    OutTable.objects.create(**data_dict)


def deleteOutTable(nid):
    OutTable.objects.filter(id=nid).delete()


def editOutTable(nid, data_dict):
    OutTable.objects.filter(id=nid).update(**data_dict)


def outTableList(data_dict):
    data_set = OutTable.objects.filter(**data_dict)
    return data_set


def newTechResearchInfo(data_dict):
    return NewTechResearch.objects.filter(**data_dict).first()


def insertNewTechResearch(data_dict):
    NewTechResearch.objects.create(**data_dict)


def deleteNewTechResearch(nid):
    NewTechResearch.objects.filter(id=nid).delete()


def editNewTechResearch(nid, data_dict):
    NewTechResearch.objects.filter(id=nid).update(**data_dict)


def newTechResearchList(data_dict):
    data_set = NewTechResearch.objects.filter(**data_dict)
    return data_set


def newTechAwardInfo(data_dict):
    return NewTechAward.objects.filter(**data_dict).first()


def insertNewTechAward(data_dict):
    NewTechAward.objects.create(**data_dict)


def deleteNewTechAward(nid):
    NewTechAward.objects.filter(id=nid).delete()


def editNewTechAward(nid, data_dict):
    NewTechAward.objects.filter(id=nid).update(**data_dict)


def newTechAwardList(data_dict):
    data_set = NewTechAward.objects.filter(**data_dict)
    return data_set


def info_shoushuzizhi(data_dict):
    return shoushuzizhi.objects.filter(**data_dict).first()


def insert_shoushuzizhi(data_dict):
    shoushuzizhi.objects.create(**data_dict)


def delete_shoushuzizhi(nid):
    shoushuzizhi.objects.filter(id=nid).delete()


def edit_shoushuzizhi(nid, data_dict):
    shoushuzizhi.objects.filter(id=nid).update(**data_dict)


def list_shoushuzizhi(data_dict):
    data_set = shoushuzizhi.objects.filter(**data_dict)
    return data_set


def info_chufang_shengwuyuxueyezhiji(data_dict):
    return chufang_shengwuyuxueyezhiji.objects.filter(**data_dict).first()


def insert_chufang_shengwuyuxueyezhiji(data_dict):
    chufang_shengwuyuxueyezhiji.objects.create(**data_dict)


def delete_chufang_shengwuyuxueyezhiji(nid):
    chufang_shengwuyuxueyezhiji.objects.filter(id=nid).delete()


def edit_chufang_shengwuyuxueyezhiji(nid, data_dict):
    chufang_shengwuyuxueyezhiji.objects.filter(id=nid).update(**data_dict)


def list_chufang_shengwuyuxueyezhiji(data_dict):
    data_set = chufang_shengwuyuxueyezhiji.objects.filter(**data_dict)
    return data_set


def info_chufang_putongchufangquan(data_dict):
    return chufang_putongchufangquan.objects.filter(**data_dict).first()


def insert_chufang_putongchufangquan(data_dict):
    chufang_putongchufangquan.objects.create(**data_dict)


def delete_chufang_putongchufangquan(nid):
    chufang_putongchufangquan.objects.filter(id=nid).delete()


def edit_chufang_putongchufangquan(nid, data_dict):
    chufang_putongchufangquan.objects.filter(id=nid).update(**data_dict)


def list_chufang_putongchufangquan(data_dict):
    data_set = chufang_putongchufangquan.objects.filter(**data_dict)
    return data_set


def info_chufang_pizhijisuleiyaowu(data_dict):
    return chufang_pizhijisuleiyaowu.objects.filter(**data_dict).first()


def insert_chufang_pizhijisuleiyaowu(data_dict):
    chufang_pizhijisuleiyaowu.objects.create(**data_dict)


def delete_chufang_pizhijisuleiyaowu(nid):
    chufang_pizhijisuleiyaowu.objects.filter(id=nid).delete()


def edit_chufang_pizhijisuleiyaowu(nid, data_dict):
    chufang_pizhijisuleiyaowu.objects.filter(id=nid).update(**data_dict)


def list_chufang_pizhijisuleiyaowu(data_dict):
    data_set = chufang_pizhijisuleiyaowu.objects.filter(**data_dict)
    return data_set


def info_chufang_changwaiyingyangzhiji(data_dict):
    return chufang_changwaiyingyangzhiji.objects.filter(**data_dict).first()


def insert_chufang_changwaiyingyangzhiji(data_dict):
    chufang_changwaiyingyangzhiji.objects.create(**data_dict)


def delete_chufang_changwaiyingyangzhiji(nid):
    chufang_changwaiyingyangzhiji.objects.filter(id=nid).delete()


def edit_chufang_changwaiyingyangzhiji(nid, data_dict):
    chufang_changwaiyingyangzhiji.objects.filter(id=nid).update(**data_dict)


def list_chufang_changwaiyingyangzhiji(data_dict):
    data_set = chufang_changwaiyingyangzhiji.objects.filter(**data_dict)
    return data_set


def info_chufang_baogaoqianziquan(data_dict):
    return chufang_baogaoqianziquan.objects.filter(**data_dict).first()


def insert_chufang_baogaoqianziquan(data_dict):
    chufang_baogaoqianziquan.objects.create(**data_dict)


def delete_chufang_baogaoqianziquan(nid):
    chufang_baogaoqianziquan.objects.filter(id=nid).delete()


def edit_chufang_baogaoqianziquan(nid, data_dict):
    chufang_baogaoqianziquan.objects.filter(id=nid).update(**data_dict)


def list_chufang_baogaoqianziquan(data_dict):
    data_set = chufang_baogaoqianziquan.objects.filter(**data_dict)
    return data_set


def info_chufang_mazuijingshen(data_dict):
    return chufang_mazuijingshen.objects.filter(**data_dict).first()


def insert_chufang_mazuijingshen(data_dict):
    chufang_mazuijingshen.objects.create(**data_dict)


def delete_chufang_mazuijingshen(nid):
    chufang_mazuijingshen.objects.filter(id=nid).delete()


def edit_chufang_mazuijingshen(nid, data_dict):
    chufang_mazuijingshen.objects.filter(id=nid).update(**data_dict)


def list_chufang_mazuijingshen(data_dict):
    data_set = chufang_mazuijingshen.objects.filter(**data_dict)
    return data_set


def info_chufang_kangzhongliu(data_dict):
    return chufang_kangzhongliu.objects.filter(**data_dict).first()


def insert_chufang_kangzhongliu(data_dict):
    chufang_kangzhongliu.objects.create(**data_dict)


def delete_chufang_kangzhongliu(nid):
    chufang_kangzhongliu.objects.filter(id=nid).delete()


def edit_chufang_kangzhongliu(nid, data_dict):
    chufang_kangzhongliu.objects.filter(id=nid).update(**data_dict)


def list_chufang_kangzhongliu(data_dict):
    data_set = chufang_kangzhongliu.objects.filter(**data_dict)
    return data_set


def info_chufang_kangjunyaowu(data_dict):
    return chufang_kangjunyaowu.objects.filter(**data_dict).first()


def insert_chufang_kangjunyaowu(data_dict):
    chufang_kangjunyaowu.objects.create(**data_dict)


def delete_chufang_kangjunyaowu(nid):
    chufang_kangjunyaowu.objects.filter(id=nid).delete()


def edit_chufang_kangjunyaowu(nid, data_dict):
    chufang_kangjunyaowu.objects.filter(id=nid).update(**data_dict)


def list_chufang_kangjunyaowu(data_dict):
    data_set = chufang_kangjunyaowu.objects.filter(**data_dict)
    return data_set


def info_chufang_yongxuezizhi(data_dict):
    return chufang_yongxuezizhi.objects.filter(**data_dict).first()


def insert_chufang_yongxuezizhi(data_dict):
    chufang_yongxuezizhi.objects.create(**data_dict)


def delete_chufang_yongxuezizhi(nid):
    chufang_yongxuezizhi.objects.filter(id=nid).delete()


def edit_chufang_yongxuezizhi(nid, data_dict):
    chufang_yongxuezizhi.objects.filter(id=nid).update(**data_dict)


def list_chufang_yongxuezizhi(data_dict):
    data_set = chufang_yongxuezizhi.objects.filter(**data_dict)
    return data_set


def info_chufang_shouquan(data_dict):
    return chufang_shouquan.objects.filter(**data_dict).first()


def insert_chufang_shouquan(data_dict):
    chufang_shouquan.objects.create(**data_dict)


def delete_chufang_shouquan(nid):
    chufang_shouquan.objects.filter(id=nid).delete()


def edit_chufang_shouquan(nid, data_dict):
    chufang_shouquan.objects.filter(id=nid).update(**data_dict)


def list_chufang_shouquan(data_dict):
    data_set = chufang_shouquan.objects.filter(**data_dict)
    return data_set


def connect_db():
    db = pymysql.connect(host="localhost", user="root", password="abcddjs921005", db="DoctorRecordsDatabase",
                         charset="utf8")
    cursor = db.cursor()
    return db, cursor


def userInfo(data_dict):
    return DoctorInfo.objects.filter(**data_dict).first()


def insertUser(data_dict):
    DoctorInfo.objects.create(**data_dict)
    return DoctorInfo.objects.filter(**data_dict).first()


def deleteUser(nid):
    return DoctorInfo.objects.filter(id=nid).delete()


def editUser(nid, data_dict):
    DoctorInfo.objects.filter(id=nid).update(**data_dict)


def userList(data_dict, type_dict):
    # user_set = {}
    data_temp = {}
    print('data_dict')
    print(str(data_dict))
    if ('search' in data_dict) or ('search' in type_dict):
        if 'search' in data_dict:
            data_temp[data_dict["search_type"] + '__contains'] = data_dict["search"]
        if 'search' in type_dict:
            data_temp[type_dict["search_type"] + '__contains'] = type_dict["search"]
        user_set = DoctorInfo.objects.filter(**data_temp)
    else:
        user_set = DoctorInfo.objects.all()
    # user_set = user_set[slice(int(data_dict['pageStart']), int(data_dict['pageStart'])+int(data_dict['pagesize']))]
    return user_set


def departInfo(data_dict):
    return Department.objects.filter(**data_dict).first()


def insertDepart(data_dict):
    Department.objects.create(**data_dict)


def deleteDepart(nid):
    Department.objects.filter(id=nid).delete()


def editDepart(nid, data_dict):
    Department.objects.filter(id=nid).update(**data_dict)


def departList(data_dict):
    data_temp = {}
    if 'search' in data_dict:
        data_temp[data_dict["search_type"] + '__contains'] = data_dict["search"]
        depart_set = Department.objects.filter(**data_temp)
    else:
        depart_set = Department.objects.all()
    # depart_set = depart_set[slice(int(data_dict['pageStart']), int(data_dict['pageStart'])+int(data_dict['pagesize']))]
    return depart_set

# def saveImg(request):
#     new_img = Avatar(
#         photo=request.FILES.get('photo'),  # 拿到图片
#         user=request.FILES.get('photo').name  # 拿到图片的名字
#     )
#     new_img.save()  # 保存图片
