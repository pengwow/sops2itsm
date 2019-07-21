# -*- coding: utf-8 -*-
from conf.default import SITE_URL
from common.mymako import render_mako_context, render_json
from django.views.decorators.csrf import csrf_exempt
from account.decorators import login_exempt
from django.http import (
    HttpResponse,
    HttpResponseRedirect,
)


def home(request):
    """
    首页
    """
    return HttpResponseRedirect(SITE_URL + 'business/home/' + str(2) + '/')
    # return render_mako_context(request, '/home_application/home.html')


def dev_guide(request):
    """
    开发指引
    """
    return render_mako_context(request, '/home_application/dev_guide.html')


def contactus(request):
    """
    联系我们
    """
    return render_mako_context(request, '/home_application/contact.html')


@login_exempt
def test(request):
    """

    :param request:
    :return:
    """
    test_dict = {
        "business": {"always_use_executor": False, "cc_company": "", "cc_id": 3, "cc_name": "蓝鲸测试001", "cc_owner": "",
                     "executor": "jiaohongtao", "id": 2, "life_cycle": "2",
                     "resource_uri": "/o/bk_sops/api/v3/business/3/", "time_zone": "Asia/Shanghai"},
        "category": "OpsTools", "category_name": "运维工具", "create_time": "2019-02-25 09:43:17 +0800",
        "creator_name": "jiaohongtao", "edit_time": "2019-06-16 15:03:50 +0800", "editor_name": "liupeng", "id": 7,
        "is_deleted": False, "name": "业务发布流程", "notify_receivers": "{\"receiver_group\":[],\"more_receiver\":\"\"}",
        "notify_type": "[]", "pipeline_template": "",
        "pipeline_tree": "{\"activities\":{\"node236602b2d9efe2fb9cbc4f7a32f2\":{\"outgoing\":\"lineb2f0d2dcfa476f47413ac5f51e24\",\"incoming\":\"linef7d759f50fe4546e4e3f3ba8e386\",\"name\":\"\\u5feb\\u901f\\u6267\\u884c\\u811a\\u672c\",\"error_ignorable\":false,\"component\":{\"code\":\"job_fast_execute_script\",\"data\":{\"job_account\":{\"hook\":true,\"value\":\"${job_account}\"},\"job_script_timeout\":{\"hook\":false,\"value\":\"\"},\"job_ip_list\":{\"hook\":true,\"value\":\"${job_ip_list}\"},\"job_content\":{\"hook\":false,\"value\":\"echo \\\"jiao001\\\"\"},\"job_script_type\":{\"hook\":false,\"value\":\"1\"},\"job_script_param\":{\"hook\":false,\"value\":\"\"}}},\"stage_name\":\"\\u6b65\\u9aa41\",\"optional\":false,\"type\":\"ServiceActivity\",\"id\":\"node236602b2d9efe2fb9cbc4f7a32f2\",\"loop\":null},\"node59241ba112a2012247bcedf1d664\":{\"outgoing\":\"line57779892cd87290ada0046676916\",\"incoming\":\"lineb2f0d2dcfa476f47413ac5f51e24\",\"name\":\"\\u5feb\\u901f\\u5206\\u53d1\\u6587\\u4ef6\",\"error_ignorable\":false,\"component\":{\"code\":\"job_fast_push_file\",\"data\":{\"job_target_path\":{\"hook\":true,\"value\":\"${job_target_path}\"},\"job_account\":{\"hook\":true,\"value\":\"${job_account}\"},\"job_ip_list\":{\"hook\":true,\"value\":\"${job_ip_list}\"},\"job_source_files\":{\"hook\":true,\"value\":\"${job_source_files}\"}}},\"stage_name\":\"\\u6b65\\u9aa41\",\"optional\":false,\"type\":\"ServiceActivity\",\"id\":\"node59241ba112a2012247bcedf1d664\",\"loop\":null}},\"end_event\":{\"incoming\":\"line57779892cd87290ada0046676916\",\"outgoing\":\"\",\"type\":\"EmptyEndEvent\",\"id\":\"node1421ca81378eaced1db32c560e03\",\"name\":\"\"},\"outputs\":[],\"flows\":{\"lineb2f0d2dcfa476f47413ac5f51e24\":{\"is_default\":false,\"source\":\"node236602b2d9efe2fb9cbc4f7a32f2\",\"id\":\"lineb2f0d2dcfa476f47413ac5f51e24\",\"target\":\"node59241ba112a2012247bcedf1d664\"},\"linef7d759f50fe4546e4e3f3ba8e386\":{\"is_default\":false,\"source\":\"nodea9a4a70001bd5cc4af934e301cea\",\"id\":\"linef7d759f50fe4546e4e3f3ba8e386\",\"target\":\"node236602b2d9efe2fb9cbc4f7a32f2\"},\"line57779892cd87290ada0046676916\":{\"is_default\":false,\"source\":\"node59241ba112a2012247bcedf1d664\",\"id\":\"line57779892cd87290ada0046676916\",\"target\":\"node1421ca81378eaced1db32c560e03\"}},\"gateways\":{},\"line\":[{\"source\":{\"id\":\"nodea9a4a70001bd5cc4af934e301cea\",\"arrow\":\"Right\"},\"target\":{\"id\":\"node236602b2d9efe2fb9cbc4f7a32f2\",\"arrow\":\"Left\"},\"id\":\"linef7d759f50fe4546e4e3f3ba8e386\"},{\"source\":{\"id\":\"node236602b2d9efe2fb9cbc4f7a32f2\",\"arrow\":\"Right\"},\"target\":{\"id\":\"node59241ba112a2012247bcedf1d664\",\"arrow\":\"Left\"},\"id\":\"lineb2f0d2dcfa476f47413ac5f51e24\"},{\"source\":{\"id\":\"node59241ba112a2012247bcedf1d664\",\"arrow\":\"Right\"},\"target\":{\"id\":\"node1421ca81378eaced1db32c560e03\",\"arrow\":\"Left\"},\"id\":\"line57779892cd87290ada0046676916\"}],\"start_event\":{\"incoming\":\"\",\"outgoing\":\"linef7d759f50fe4546e4e3f3ba8e386\",\"type\":\"EmptyStartEvent\",\"id\":\"nodea9a4a70001bd5cc4af934e301cea\",\"name\":\"\"},\"constants\":{\"${job_ip_list}\":{\"source_tag\":\"job_fast_execute_script.job_ip_list\",\"source_info\":{\"node236602b2d9efe2fb9cbc4f7a32f2\":[\"job_ip_list\"],\"node59241ba112a2012247bcedf1d664\":[\"job_ip_list\"]},\"name\":\"\\u76ee\\u6807IP\",\"index\":0,\"custom_type\":\"\",\"value\":\"10.20.8.138\",\"show_type\":\"show\",\"source_type\":\"component_inputs\",\"key\":\"${job_ip_list}\",\"validation\":\"\",\"desc\":\"\"},\"${job_account}\":{\"source_tag\":\"job_fast_execute_script.job_account\",\"source_info\":{\"node236602b2d9efe2fb9cbc4f7a32f2\":[\"job_account\"],\"node59241ba112a2012247bcedf1d664\":[\"job_account\"]},\"name\":\"\\u76ee\\u6807\\u8d26\\u6237\",\"index\":1,\"custom_type\":\"\",\"value\":\"root\",\"show_type\":\"show\",\"source_type\":\"component_inputs\",\"key\":\"${job_account}\",\"validation\":\"\",\"desc\":\"\"},\"${job_source_files}\":{\"source_tag\":\"job_fast_push_file.job_source_files\",\"source_info\":{\"node59241ba112a2012247bcedf1d664\":[\"job_source_files\"]},\"name\":\"\\u6e90\\u6587\\u4ef6\",\"index\":2,\"custom_type\":\"\",\"value\":[],\"show_type\":\"show\",\"source_type\":\"component_inputs\",\"key\":\"${job_source_files}\",\"validation\":\"\",\"desc\":\"\"},\"${ddddd}\":{\"source_tag\":\"\",\"source_info\":{},\"name\":\"ddddd\",\"index\":4,\"custom_type\":\"textarea\",\"value\":\"dddddddddddddddd\\nddddddddddd\\ndddddddddddddd\",\"show_type\":\"show\",\"source_type\":\"custom\",\"validator\":[],\"key\":\"${ddddd}\",\"desc\":\"\",\"validation\":\"\",\"is_meta\":false},\"${job_target_path}\":{\"source_tag\":\"job_fast_push_file.job_target_path\",\"source_info\":{\"node59241ba112a2012247bcedf1d664\":[\"job_target_path\"]},\"name\":\"\\u76ee\\u6807\\u8def\\u5f84\",\"index\":3,\"custom_type\":\"\",\"value\":\"\",\"show_type\":\"show\",\"source_type\":\"component_inputs\",\"key\":\"${job_target_path}\",\"validation\":\"\",\"desc\":\"\"}},\"location\":[{\"stage_name\":\"\\u6b65\\u9aa41\",\"name\":\"\",\"y\":170,\"x\":740,\"type\":\"endpoint\",\"id\":\"node1421ca81378eaced1db32c560e03\"},{\"stage_name\":\"\\u6b65\\u9aa41\",\"name\":\"\",\"y\":155,\"x\":105,\"type\":\"startpoint\",\"id\":\"nodea9a4a70001bd5cc4af934e301cea\"},{\"stage_name\":\"\\u6b65\\u9aa41\",\"name\":\"\\u5feb\\u901f\\u6267\\u884c\\u811a\\u672c\",\"y\":155,\"x\":320,\"type\":\"tasknode\",\"id\":\"node236602b2d9efe2fb9cbc4f7a32f2\"},{\"stage_name\":\"\\u6b65\\u9aa41\",\"name\":\"\\u5feb\\u901f\\u5206\\u53d1\\u6587\\u4ef6\",\"y\":155,\"x\":525,\"type\":\"tasknode\",\"id\":\"node59241ba112a2012247bcedf1d664\"}]}",
        "resource_uri": "/o/bk_sops/api/v3/template/7/",
        "subprocess_info": {"details": [], "subproc_has_update": False}, "template_id": 7, "time_out": 20,
        "version": "95be3672227a4ec91007a8eebff867e5"}
    return render_json(test_dict)
