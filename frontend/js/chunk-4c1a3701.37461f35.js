(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-4c1a3701"],{"83ec":function(t,e,a){"use strict";a.r(e);var i=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"m-activity_details"},[a("el-form",{ref:"dataForm",attrs:{rules:t.rules,model:t.temp,"label-position":"left","label-width":"100px"}},[a("el-form-item",{staticClass:"el_form",attrs:{label:"部门名:"}},[a("el-input",{model:{value:t.temp.title,callback:function(e){t.$set(t.temp,"title",e)},expression:"temp.title"}})],1),a("el-form-item",{staticClass:"el_form",attrs:{label:"账号:"}},[a("el-input",{model:{value:t.temp.account,callback:function(e){t.$set(t.temp,"account",e)},expression:"temp.account"}})],1),a("el-form-item",{staticClass:"el_form",attrs:{label:"密码:"}},[a("el-input",{attrs:{type:"text"},model:{value:t.temp.password,callback:function(e){t.$set(t.temp,"password",e)},expression:"temp.password"}})],1),a("div",{staticStyle:{"text-align":"center"}},[a("el-button",{staticStyle:{"margin-right":"40px","min-width":"120px"},attrs:{type:"primary"},on:{click:t.handleEditDepart}},[t._v("确定")]),a("el-button",{staticStyle:{"min-width":"120px"},attrs:{type:"info"},on:{click:t.handleJumpLists}},[t._v("取消")])],1)],1)],1)},n=[],r=a("ad8f"),s=[{key:"processing",display_name:"进行中"},{key:"nostart",display_name:"未开始"},{key:"ended",display_name:"已结束"}],l=[{key:"1",display_name:"普通权限"},{key:"2",display_name:"高级权限"},{key:"3",display_name:"最高权限"}],o=[{key:"1",display_name:"事业发展科"},{key:"2",display_name:"小区1"},{key:"3",display_name:"小区2"},{key:"4",display_name:"小区3"}],c={name:"UserList",components:{},filters:{statusFilter:function(t){var e={published:"success",draft:"gray",deleted:"danger"};return e[t]}},data:function(){return{departmentOptions:o,TypeOptions:l,activityStatusOptions:s,rules:{type:[{required:!0,message:"type is required",trigger:"change"}],timestamp:[{type:"date",required:!0,message:"timestamp is required",trigger:"change"}],title:[{required:!0,message:"title is required",trigger:"blur"}]},temp:{title:"",account:"",password:""},total:0,tableKey:0,list:null,depart:null,listLoading:!0,listQuery:{page:1,limit:20,importance:void 0,title:void 0,type:void 0,sort:"+id"}}},created:function(){this.fetchData()},methods:{fetchData:function(){var t=this;console.log("this.$route.params",this.$route.params),this.listLoading=!0,Object(r["d"])({id:this.$route.params.id}).then((function(e){console.log("depart details info response",e),t.temp=e.data}))},departEdit:function(){var t=this;Object(r["c"])(this.temp).then((function(e){"success"===e.data&&t.$router.push("/department/department-list/")}))},handleJumpLists:function(){this.$router.push("/user/user-list/")},handleEditDepart:function(){this.departEdit()}}},d=c,u=a("2877"),p=Object(u["a"])(d,i,n,!1,null,null,null);e["default"]=p.exports},ad8f:function(t,e,a){"use strict";a.d(e,"g",(function(){return r})),a.d(e,"e",(function(){return s})),a.d(e,"d",(function(){return l})),a.d(e,"b",(function(){return o})),a.d(e,"c",(function(){return c})),a.d(e,"a",(function(){return d}));var i=a("b775"),n=a("5f87");function r(t){return t.token=Object(n["c"])(),Object(i["a"])({url:"/user/list",method:"get",params:t})}function s(t){return t.token=Object(n["c"])(),Object(i["a"])({url:"/depart/list",method:"get",params:t})}function l(t){return t.token=Object(n["c"])(),Object(i["a"])({url:"/depart/details",method:"get",params:t})}function o(t){return t.token=Object(n["c"])(),Object(i["a"])({url:"/depart/delete",method:"get",params:t})}function c(t){return t.token=Object(n["c"])(),Object(i["a"])({url:"/depart/edit",method:"post",data:t})}function d(t){return t.token=Object(n["c"])(),Object(i["a"])({url:"/depart/add",method:"post",data:t})}}}]);