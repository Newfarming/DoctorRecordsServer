# Generated by Django 4.1.3 on 2024-03-05 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DoctorRecordsServerApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chufang_baogaoqianziquan',
            name='get_year',
            field=models.CharField(max_length=1024, verbose_name='年度'),
        ),
        migrations.AlterField(
            model_name='chufang_baogaoqianziquan',
            name='other',
            field=models.CharField(max_length=1024, verbose_name='其他'),
        ),
        migrations.AlterField(
            model_name='chufang_changwaiyingyangzhiji',
            name='get_year',
            field=models.CharField(max_length=1024, verbose_name='年度'),
        ),
        migrations.AlterField(
            model_name='chufang_changwaiyingyangzhiji',
            name='other',
            field=models.CharField(max_length=1024, verbose_name='其他'),
        ),
        migrations.AlterField(
            model_name='chufang_kangjunyaowu',
            name='get_year',
            field=models.CharField(max_length=1024, verbose_name='年度'),
        ),
        migrations.AlterField(
            model_name='chufang_kangjunyaowu',
            name='other',
            field=models.CharField(max_length=1024, verbose_name='其他'),
        ),
        migrations.AlterField(
            model_name='chufang_kangzhongliu',
            name='get_year',
            field=models.CharField(max_length=1024, verbose_name='年度'),
        ),
        migrations.AlterField(
            model_name='chufang_kangzhongliu',
            name='other',
            field=models.CharField(max_length=1024, verbose_name='其他'),
        ),
        migrations.AlterField(
            model_name='chufang_mazuijingshen',
            name='get_year',
            field=models.CharField(max_length=1024, verbose_name='年度'),
        ),
        migrations.AlterField(
            model_name='chufang_mazuijingshen',
            name='other',
            field=models.CharField(max_length=1024, verbose_name='其他'),
        ),
        migrations.AlterField(
            model_name='chufang_pizhijisuleiyaowu',
            name='get_year',
            field=models.CharField(max_length=1024, verbose_name='年度'),
        ),
        migrations.AlterField(
            model_name='chufang_pizhijisuleiyaowu',
            name='other',
            field=models.CharField(max_length=1024, verbose_name='其他'),
        ),
        migrations.AlterField(
            model_name='chufang_putongchufangquan',
            name='get_year',
            field=models.CharField(max_length=1024, verbose_name='年度'),
        ),
        migrations.AlterField(
            model_name='chufang_putongchufangquan',
            name='other',
            field=models.CharField(max_length=1024, verbose_name='其他'),
        ),
        migrations.AlterField(
            model_name='chufang_shengwuyuxueyezhiji',
            name='get_year',
            field=models.CharField(max_length=1024, verbose_name='年度'),
        ),
        migrations.AlterField(
            model_name='chufang_shengwuyuxueyezhiji',
            name='other',
            field=models.CharField(max_length=1024, verbose_name='其他'),
        ),
        migrations.AlterField(
            model_name='chufang_shouquan',
            name='get_year',
            field=models.CharField(max_length=1024, verbose_name='年度'),
        ),
        migrations.AlterField(
            model_name='chufang_shouquan',
            name='other',
            field=models.CharField(max_length=1024, verbose_name='其他'),
        ),
        migrations.AlterField(
            model_name='chufang_shouquan',
            name='shouquanpic',
            field=models.CharField(max_length=1024, verbose_name='相关授权表'),
        ),
        migrations.AlterField(
            model_name='chufang_yongxuezizhi',
            name='get_year',
            field=models.CharField(max_length=1024, verbose_name='年度'),
        ),
        migrations.AlterField(
            model_name='chufang_yongxuezizhi',
            name='other',
            field=models.CharField(max_length=1024, verbose_name='其他'),
        ),
        migrations.AlterField(
            model_name='department',
            name='account',
            field=models.CharField(max_length=1024, verbose_name='账号'),
        ),
        migrations.AlterField(
            model_name='department',
            name='password',
            field=models.CharField(max_length=1024, verbose_name='密码'),
        ),
        migrations.AlterField(
            model_name='department',
            name='permission_type',
            field=models.CharField(max_length=1024, verbose_name='权限类型'),
        ),
        migrations.AlterField(
            model_name='department',
            name='title',
            field=models.CharField(max_length=1024, verbose_name='科室名称'),
        ),
        migrations.AlterField(
            model_name='doctorinfo',
            name='academic_degree',
            field=models.CharField(max_length=1024, verbose_name='学位'),
        ),
        migrations.AlterField(
            model_name='doctorinfo',
            name='education',
            field=models.CharField(max_length=1024, verbose_name='学历'),
        ),
        migrations.AlterField(
            model_name='doctorinfo',
            name='graduated_school',
            field=models.CharField(max_length=1024, verbose_name='毕业院校'),
        ),
        migrations.AlterField(
            model_name='doctorinfo',
            name='major',
            field=models.CharField(max_length=1024, verbose_name='专业'),
        ),
        migrations.AlterField(
            model_name='doctorinfo',
            name='name',
            field=models.CharField(max_length=1024, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='doctorinfo',
            name='phone',
            field=models.CharField(max_length=1024, verbose_name='联系电话'),
        ),
        migrations.AlterField(
            model_name='doctorinfo',
            name='sex',
            field=models.CharField(max_length=1024, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='doctorinfo',
            name='surgical_qualification',
            field=models.CharField(max_length=1024, verbose_name='手术资质'),
        ),
        migrations.AlterField(
            model_name='doctorinfo',
            name='surgical_qualification_certificate_pic',
            field=models.CharField(max_length=1024, verbose_name='手术资质授权表'),
        ),
        migrations.AlterField(
            model_name='newtechaward',
            name='award_certificate_pic',
            field=models.CharField(max_length=1024, verbose_name='获奖证书'),
        ),
        migrations.AlterField(
            model_name='newtechaward',
            name='award_name',
            field=models.CharField(max_length=1024, verbose_name='获奖名称'),
        ),
        migrations.AlterField(
            model_name='newtechaward',
            name='award_rank',
            field=models.CharField(max_length=1024, verbose_name='获奖级别'),
        ),
        migrations.AlterField(
            model_name='newtechaward',
            name='get_year',
            field=models.CharField(max_length=1024, verbose_name='获奖年度'),
        ),
        migrations.AlterField(
            model_name='newtechresearch',
            name='approved_time',
            field=models.CharField(max_length=1024, verbose_name='获取开展时间'),
        ),
        migrations.AlterField(
            model_name='newtechresearch',
            name='name',
            field=models.CharField(max_length=1024, verbose_name='项目名称'),
        ),
        migrations.AlterField(
            model_name='newtechresearch',
            name='to_nomal_time',
            field=models.CharField(max_length=1024, verbose_name='转常规技术开展时间'),
        ),
        migrations.AlterField(
            model_name='obtainpatents',
            name='get_time',
            field=models.CharField(max_length=1024, verbose_name='年度'),
        ),
        migrations.AlterField(
            model_name='obtainpatents',
            name='name',
            field=models.CharField(max_length=1024, verbose_name='专利名称'),
        ),
        migrations.AlterField(
            model_name='obtainpatents',
            name='patents_certificate_pic',
            field=models.CharField(max_length=1024, verbose_name='专利证书'),
        ),
        migrations.AlterField(
            model_name='obtainpatents',
            name='type',
            field=models.CharField(max_length=1024, verbose_name='专利类型'),
        ),
        migrations.AlterField(
            model_name='outtable',
            name='out_study_meeting',
            field=models.CharField(max_length=1024, verbose_name='学习会议名称'),
        ),
        migrations.AlterField(
            model_name='outtable',
            name='out_study_place',
            field=models.CharField(max_length=1024, verbose_name='外出学习地点'),
        ),
        migrations.AlterField(
            model_name='professionaltitle',
            name='certificate_number',
            field=models.CharField(max_length=1024, verbose_name='聘任时间'),
        ),
        migrations.AlterField(
            model_name='professionaltitle',
            name='name',
            field=models.CharField(max_length=1024, verbose_name='职称名'),
        ),
        migrations.AlterField(
            model_name='researchaward',
            name='award_certificate_pic',
            field=models.CharField(max_length=1024, verbose_name='获奖证书'),
        ),
        migrations.AlterField(
            model_name='researchaward',
            name='award_name',
            field=models.CharField(max_length=1024, verbose_name='获奖名称'),
        ),
        migrations.AlterField(
            model_name='researchaward',
            name='award_rank',
            field=models.CharField(max_length=1024, verbose_name='获奖级别'),
        ),
        migrations.AlterField(
            model_name='researchaward',
            name='award_time',
            field=models.CharField(max_length=1024, verbose_name='获奖年度'),
        ),
        migrations.AlterField(
            model_name='researchpapers',
            name='journal_name',
            field=models.CharField(max_length=1024, verbose_name='期刊名称'),
        ),
        migrations.AlterField(
            model_name='researchpapers',
            name='project_name',
            field=models.CharField(max_length=1024, verbose_name='项目名称'),
        ),
        migrations.AlterField(
            model_name='researchpapers',
            name='project_rank',
            field=models.CharField(max_length=1024, verbose_name='项目类型'),
        ),
        migrations.AlterField(
            model_name='researchproject',
            name='start_time',
            field=models.CharField(max_length=1024, verbose_name='立项时间'),
        ),
        migrations.AlterField(
            model_name='researchproject',
            name='start_type',
            field=models.CharField(max_length=1024, verbose_name='立项类型'),
        ),
        migrations.AlterField(
            model_name='researchproject',
            name='title',
            field=models.CharField(max_length=1024, verbose_name='题目'),
        ),
        migrations.AlterField(
            model_name='shoushuzizhi',
            name='get_year',
            field=models.CharField(max_length=1024, verbose_name='年度'),
        ),
        migrations.AlterField(
            model_name='shoushuzizhi',
            name='other',
            field=models.CharField(max_length=1024, verbose_name='其他'),
        ),
        migrations.AlterField(
            model_name='shoushuzizhi',
            name='surgical_qualification_certificate_pic',
            field=models.CharField(max_length=1024, verbose_name='手术资质授权表'),
        ),
        migrations.AlterField(
            model_name='studytable',
            name='study_certificate_pic',
            field=models.CharField(max_length=1024, verbose_name='进修证照片'),
        ),
        migrations.AlterField(
            model_name='studytable',
            name='study_hospital',
            field=models.CharField(max_length=1024, verbose_name='进修医院'),
        ),
        migrations.AlterField(
            model_name='studytable',
            name='study_major',
            field=models.CharField(max_length=1024, verbose_name='进修专业'),
        ),
        migrations.AlterField(
            model_name='studytable',
            name='study_time',
            field=models.CharField(max_length=1024, verbose_name='进修时间'),
        ),
    ]
