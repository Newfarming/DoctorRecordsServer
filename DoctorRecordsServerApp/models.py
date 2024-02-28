from django.db import models


# Create your models here.
class Department(models.Model):
    # 科室表
    title = models.CharField(verbose_name="科室名称", max_length=1024)
    account = models.CharField(verbose_name="账号", max_length=1024)
    password = models.CharField(verbose_name="密码", max_length=1024)
    permission_type = models.CharField(verbose_name="权限类型", max_length=1024)

    def __str__(self):
        # 解决ModelForm的外键引用返回对象的问题.
        return self.title


class DoctorInfo(models.Model):
    # 医生档案主表
    name = models.CharField(verbose_name="姓名", max_length=1024)
    sex = models.CharField(verbose_name="性别", max_length=1024)
    education = models.CharField(verbose_name="学历", max_length=1024)
    academic_degree = models.CharField(verbose_name="学位", max_length=1024)
    major = models.CharField(verbose_name="专业", max_length=1024)
    graduated_school = models.CharField(verbose_name="毕业院校", max_length=1024)
    working_time = models.DateField(verbose_name="参加工作时间")
    phone = models.CharField(verbose_name="联系电话", max_length=1024)
    birthday = models.DateField(verbose_name="出生年月")
    depart = models.ForeignKey(verbose_name="科室", to="Department", to_field="id", on_delete=models.CASCADE)
    surgical_qualification = models.CharField(verbose_name="手术资质", max_length=1024)
    surgical_qualification_1 = models.BooleanField(default=False)
    surgical_qualification_2 = models.BooleanField(default=False)
    surgical_qualification_3 = models.BooleanField(default=False)
    surgical_qualification_4 = models.BooleanField(default=False)
    surgical_qualification_certificate_pic = models.CharField(verbose_name="手术资质授权表", max_length=1024)
    # 处方-普通处方权
    prescription_normal = models.BooleanField(default=False)
    # 处方-抗菌药物-限制级
    prescription_Antibacterials_restricted = models.BooleanField(default=False)
    # 处方-抗菌药物-非限制级
    prescription_Antibacterials_unrestricted = models.BooleanField(default=False)
    # 处方-抗菌药物-特殊级抗菌药物
    prescription_Antibacterials_special = models.BooleanField(default=False)
    # 处方-抗肿瘤药物-普通级
    prescription_Antineoplastic_normal = models.BooleanField(default=False)
    # 处方-抗肿瘤药物-限制级
    prescription_Antineoplastic_limited = models.BooleanField(default=False)
    # 处方-麻醉精神类-麻醉药品
    prescription_Narcotics_Narcotic_drugs = models.BooleanField(default=False)
    # 处方-麻醉精神类-第一类精神药品
    prescription_Narcotics_Psychotropic_first = models.BooleanField(default=False)
    # 处方-麻醉精神类-第二类精神药品
    prescription_Narcotics_Psychotropic_second = models.BooleanField(default=False)
    # 处方-皮质激素类药物-短中程使用糖皮质激素
    prescription_Corticosteroids_Short_glucocorticoid = models.BooleanField(default=False)
    # 处方-皮质激素类药物-冲击疗法、长疗程使用糖皮质激素
    prescription_Corticosteroids_Long_glucocorticoid = models.BooleanField(default=False)
    # 处方-生物与血液制剂
    prescription_Biological_and_blood_preparations = models.BooleanField(default=False)
    # 处方-肠外营养制剂
    changwaiyingyangzhiji = models.BooleanField(default=False)
    # 处方-急诊用血
    jizhenyongxue = models.BooleanField(default=False)
    # 处方-平诊用血
    pingzhenyongxue = models.BooleanField(default=False)
    # 处方-用血量小于800
    yongxueliangxiaoyu800 = models.BooleanField(default=False)
    # 处方-用血量小于1600
    yongxueliangxiaoyu1600 = models.BooleanField(default=False)
    # 处方-检验报告
    jianyanbaogao = models.BooleanField(default=False)
    # 处方-检查报告
    jianchabaogao = models.BooleanField(default=False)
    # 处方-输血检验报告
    shuxuejianyanbaogao = models.BooleanField(default=False)
    # # 职称情况
    # professional_Title = models.ForeignKey(verbose_name="职称情况", to="ProfessionalTitle", to_field="id",
    #                                        on_delete=models.CASCADE)
    # # 进修情况
    # study_Table = models.ForeignKey(verbose_name="进修表", to="StudyTable", to_field="id", on_delete=models.CASCADE)
    # # 外出学习表
    # out_Table = models.ForeignKey(verbose_name="外出学习表", to="OutTable", to_field="id", on_delete=models.CASCADE)
    # # 科研项目
    # research_Project = models.ForeignKey(verbose_name="科研项目", to="ResearchProject", to_field="id",
    #                                      on_delete=models.CASCADE)
    # # 科研获奖
    # research_Award = models.ForeignKey(verbose_name="科研获奖", to="ResearchAward", to_field="id",
    #                                    on_delete=models.CASCADE)
    # # 科研论文
    # research_Papers = models.ForeignKey(verbose_name="科研论文", to="ResearchPapers", to_field="id",
    #                                     on_delete=models.CASCADE)
    # # 获取专利
    # obtain_Patents = models.ForeignKey(verbose_name="获取专利", to="ObtainPatents", to_field="id",
    #                                    on_delete=models.CASCADE)
    # # 新技术开展情况
    # new_Tech_Research = models.ForeignKey(verbose_name="新技术开展情况", to="NewTechResearch", to_field="id",
    #                                       on_delete=models.CASCADE)
    # # 新技术获奖情况
    # new_Tech_Award = models.ForeignKey(verbose_name="新技术获奖情况", to="NewTechAward", to_field="id",
    #                                    on_delete=models.CASCADE)

    def __str__(self):
        # 解决ModelForm的外键引用返回对象的问题.
        return self.name


class ProfessionalTitle(models.Model):
    # 职称表
    name = models.CharField(verbose_name="职称名", max_length=1024)
    engage_time = models.DateField(verbose_name="聘任时间")
    certificate_number = models.CharField(verbose_name="聘任时间", max_length=1024)
    # 关联医生
    doctor = models.ForeignKey(verbose_name="医生档案主表", to="DoctorInfo", to_field="id", on_delete=models.CASCADE)
    def __str__(self):
        # 解决ModelForm的外键引用返回对象的问题.
        return self.name


class StudyTable(models.Model):
    # 进修表
    study_time = models.CharField(verbose_name="进修时间", max_length=1024)
    study_hospital = models.CharField(verbose_name="进修医院", max_length=1024)
    study_major = models.CharField(verbose_name="进修专业", max_length=1024)
    study_certificate_pic = models.CharField(verbose_name="进修证照片", max_length=1024)
    # 关联医生
    doctor = models.ForeignKey(verbose_name="医生档案主表", to="DoctorInfo", to_field="id", on_delete=models.CASCADE)


class OutTable(models.Model):
    # 外出学习表
    out_study_time = models.DateField(verbose_name="外出学习时间")
    out_study_place = models.CharField(verbose_name="外出学习地点", max_length=1024)
    out_study_meeting = models.CharField(verbose_name="学习会议名称", max_length=1024)
    # 关联医生
    doctor = models.ForeignKey(verbose_name="医生档案主表", to="DoctorInfo", to_field="id", on_delete=models.CASCADE)


class ResearchProject(models.Model):
    # 科研项目
    start_time = models.CharField(verbose_name="立项时间", max_length=1024)
    start_type = models.CharField(verbose_name="立项类型", max_length=1024)
    title = models.CharField(verbose_name="题目", max_length=1024)
    # 关联医生
    doctor = models.ForeignKey(verbose_name="医生档案主表", to="DoctorInfo", to_field="id", on_delete=models.CASCADE)


class ResearchAward(models.Model):
    # 科研获奖
    award_time = models.CharField(verbose_name="获奖年度", max_length=1024)
    award_rank = models.CharField(verbose_name="获奖级别", max_length=1024)
    award_name = models.CharField(verbose_name="获奖名称", max_length=1024)
    award_certificate_pic = models.CharField(verbose_name="获奖证书", max_length=1024)
    # 关联医生
    doctor = models.ForeignKey(verbose_name="医生档案主表", to="DoctorInfo", to_field="id", on_delete=models.CASCADE)


class ResearchPapers(models.Model):
    # 科研论文
    publication_time = models.DateField(verbose_name="发表时间")
    journal_name = models.CharField(verbose_name="期刊名称", max_length=1024)
    project_name = models.CharField(verbose_name="项目名称", max_length=1024)
    project_rank = models.CharField(verbose_name="项目类型", max_length=1024)
    # 关联医生
    doctor = models.ForeignKey(verbose_name="医生档案主表", to="DoctorInfo", to_field="id", on_delete=models.CASCADE)


class ObtainPatents(models.Model):
    # 获取专利
    get_time = models.CharField(verbose_name="年度", max_length=1024)
    type = models.CharField(verbose_name="专利类型", max_length=1024)
    name = models.CharField(verbose_name="专利名称", max_length=1024)
    patents_certificate_pic = models.CharField(verbose_name="专利证书", max_length=1024)
    # 关联医生
    doctor = models.ForeignKey(verbose_name="医生档案主表", to="DoctorInfo", to_field="id", on_delete=models.CASCADE)


class NewTechResearch(models.Model):
    # 新技术开展情况
    approved_time = models.DateField(verbose_name="获取开展时间")
    to_nomal_time = models.DateField(verbose_name="转常规技术开展时间")
    name = models.CharField(verbose_name="项目名称", max_length=1024)
    # 关联医生
    doctor = models.ForeignKey(verbose_name="医生档案主表", to="DoctorInfo", to_field="id", on_delete=models.CASCADE)


class NewTechAward(models.Model):
    # 新技术获奖情况
    get_year = models.CharField(verbose_name="获奖年度", max_length=1024)
    award_rank = models.CharField(verbose_name="获奖级别", max_length=1024)
    award_name = models.CharField(verbose_name="获奖名称", max_length=1024)
    award_certificate_pic = models.CharField(verbose_name="获奖证书", max_length=1024)
    # 关联医生
    doctor = models.ForeignKey(verbose_name="医生档案主表", to="DoctorInfo", to_field="id", on_delete=models.CASCADE)


class shoushuzizhi(models.Model):
    # 手术资质
    get_year = models.CharField(verbose_name="年度", max_length=1024)
    surgical_qualification_1 = models.BooleanField(default=False)
    surgical_qualification_2 = models.BooleanField(default=False)
    surgical_qualification_3 = models.BooleanField(default=False)
    surgical_qualification_4 = models.BooleanField(default=False)
    other = models.CharField(verbose_name="其他", max_length=1024)
    surgical_qualification_certificate_pic = models.CharField(verbose_name="手术资质授权表", max_length=1024)
    # 关联医生
    doctor = models.ForeignKey(verbose_name="医生档案主表", to="DoctorInfo", to_field="id", on_delete=models.CASCADE)


class chufang_putongchufangquan(models.Model):
    # 普通处方权
    get_year = models.CharField(verbose_name="年度", max_length=1024)
    putongchufangquan = models.BooleanField(default=False)
    other = models.CharField(verbose_name="其他", max_length=1024)
    # 关联医生
    doctor = models.ForeignKey(verbose_name="医生档案主表", to="DoctorInfo", to_field="id", on_delete=models.CASCADE)


class chufang_kangjunyaowu(models.Model):
    # 抗菌药物
    get_year = models.CharField(verbose_name="年度", max_length=1024)
    feixianzhi = models.BooleanField(default=False)
    xianzhi = models.BooleanField(default=False)
    teshujikangjunyaowu = models.BooleanField(default=False)
    other = models.CharField(verbose_name="其他", max_length=1024)
    # 关联医生
    doctor = models.ForeignKey(verbose_name="医生档案主表", to="DoctorInfo", to_field="id", on_delete=models.CASCADE)


class chufang_kangzhongliu(models.Model):
    # 抗肿瘤
    get_year = models.CharField(verbose_name="年度", max_length=1024)
    putongshiyong = models.BooleanField(default=False)
    xianzhishiyong = models.BooleanField(default=False)
    other = models.CharField(verbose_name="其他", max_length=1024)
    # 关联医生
    doctor = models.ForeignKey(verbose_name="医生档案主表", to="DoctorInfo", to_field="id", on_delete=models.CASCADE)


class chufang_mazuijingshen(models.Model):
    # 麻醉精神
    get_year = models.CharField(verbose_name="年度", max_length=1024)
    mazuiyaopin = models.BooleanField(default=False)
    diyileijingshenyaopin = models.BooleanField(default=False)
    dierleijingshenyaopin = models.BooleanField(default=False)
    other = models.CharField(verbose_name="其他", max_length=1024)
    # 关联医生
    doctor = models.ForeignKey(verbose_name="医生档案主表", to="DoctorInfo", to_field="id", on_delete=models.CASCADE)


class chufang_pizhijisuleiyaowu(models.Model):
    # 皮质激素类药物
    get_year = models.CharField(verbose_name="年度", max_length=1024)
    duanzhongcheng = models.BooleanField(default=False)
    chongjiliaofachangliaocheng = models.BooleanField(default=False)
    other = models.CharField(verbose_name="其他", max_length=1024)
    # 关联医生
    doctor = models.ForeignKey(verbose_name="医生档案主表", to="DoctorInfo", to_field="id", on_delete=models.CASCADE)


class chufang_shengwuyuxueyezhiji(models.Model):
    # 生物与血液制剂
    get_year = models.CharField(verbose_name="年度", max_length=1024)
    shengwuyuxueyezhiji = models.BooleanField(default=False)
    other = models.CharField(verbose_name="其他", max_length=1024)
    # 关联医生
    doctor = models.ForeignKey(verbose_name="医生档案主表", to="DoctorInfo", to_field="id", on_delete=models.CASCADE)


class chufang_changwaiyingyangzhiji(models.Model):
    # 肠外营养制剂
    get_year = models.CharField(verbose_name="年度", max_length=1024)
    changwaiyingyangzhiji = models.BooleanField(default=False)
    other = models.CharField(verbose_name="其他", max_length=1024)
    # 关联医生
    doctor = models.ForeignKey(verbose_name="医生档案主表", to="DoctorInfo", to_field="id", on_delete=models.CASCADE)


class chufang_yongxuezizhi(models.Model):
    # 用血资质
    get_year = models.CharField(verbose_name="年度", max_length=1024)
    jizhen = models.BooleanField(default=False)
    pingzhen = models.BooleanField(default=False)
    xiaoyu800 = models.BooleanField(default=False)
    xiaoyu1600 = models.BooleanField(default=False)
    other = models.CharField(verbose_name="其他", max_length=1024)
    # 关联医生
    doctor = models.ForeignKey(verbose_name="医生档案主表", to="DoctorInfo", to_field="id", on_delete=models.CASCADE)


class chufang_baogaoqianziquan(models.Model):
    # 报告签字权
    get_year = models.CharField(verbose_name="年度", max_length=1024)
    jianyanbaogao = models.BooleanField(default=False)
    jianchabaogao = models.BooleanField(default=False)
    shuxuejianyanbaogao = models.BooleanField(default=False)
    other = models.CharField(verbose_name="其他", max_length=1024)
    # 关联医生
    doctor = models.ForeignKey(verbose_name="医生档案主表", to="DoctorInfo", to_field="id", on_delete=models.CASCADE)


class chufang_shouquan(models.Model):
    # 授权相关
    get_year = models.CharField(verbose_name="年度", max_length=1024)
    youchuangcaozuoshouquan = models.BooleanField(default=False)
    rijianshoushushouquan = models.BooleanField(default=False)
    mazuishouquan = models.BooleanField(default=False)
    other = models.CharField(verbose_name="其他", max_length=1024)
    shouquanpic = models.CharField(verbose_name="相关授权表", max_length=1024)
    # 关联医生
    doctor = models.ForeignKey(verbose_name="医生档案主表", to="DoctorInfo", to_field="id", on_delete=models.CASCADE)

# 存放图片的表
# class Avatar(models.Model):
#     user = models.CharField(max_length=100)
#     photo = models.ImageField(upload_to='photos', default='avatar.jpg')