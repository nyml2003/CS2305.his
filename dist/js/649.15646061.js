"use strict";(self["webpackChunkcs2305_his"]=self["webpackChunkcs2305_his"]||[]).push([[649],{8696:function(e,t){t.Z=(e,t)=>{const l=e.__vccOpts||e;for(const[a,n]of t)l[a]=n;return l}},5649:function(e,t,l){l.r(t),l.d(t,{default:function(){return g}});l(4119);var a=l(7279),n=l(7313),o=l(1481),u=l(6043),s=l(5448),i=l(7115);const c=e=>((0,a.dD)("data-v-4e11629c"),e=e(),(0,a.Cn)(),e),r=c((()=>(0,a._)("h2",{class:"login_title"},"登录 CS2305.HIS管理系统",-1))),d=(0,a.Uk)("→"),p={class:"login_register"},m=c((()=>(0,a._)("p",null,"Don't have a CS2305.HIS account yet?",-1))),f=(0,a.Uk)("Get started here");var _={name:"LoginView",setup(e){const t=(0,s.oR)(),l=(0,n.iH)(""),c=(0,n.iH)(""),_=async()=>{const e=await o.Z.login(c.value,l.value);console.log(e.data),!1===e.data.isRight?(0,u.bM)({title:"登录失败",message:"用户名或密码错误"}):(t.commit("setUser",e.data.user),console.log(t.state.user),i.Z.push({path:"/MyPage"}))};return(e,t)=>{const n=(0,a.up)("el-input"),o=(0,a.up)("el-form-item"),u=(0,a.up)("el-button"),s=(0,a.up)("el-col"),i=(0,a.up)("router-link"),h=(0,a.up)("el-form"),w=(0,a.up)("el-row");return(0,a.wg)(),(0,a.j4)(w,{style:{"align-items":"center","justify-content":"center",height:"100% width:100%"}},{default:(0,a.w5)((()=>[(0,a.Wm)(h,{"label-position":"top","label-width":"80px",style:{width:"fit-content"}},{default:(0,a.w5)((()=>[r,(0,a.Wm)(o,{label:"用户名"},{default:(0,a.w5)((()=>[(0,a.Wm)(n,{modelValue:c.value,"onUpdate:modelValue":t[0]||(t[0]=e=>c.value=e),placeholder:"Username"},null,8,["modelValue"])])),_:1}),(0,a.Wm)(o,{label:"密码"},{default:(0,a.w5)((()=>[(0,a.Wm)(n,{modelValue:l.value,"onUpdate:modelValue":t[1]||(t[1]=e=>l.value=e),placeholder:"Password"},null,8,["modelValue"])])),_:1}),(0,a.Wm)(o,null,{default:(0,a.w5)((()=>[(0,a.Wm)(s,{span:24,style:{"text-align":"center"}},{default:(0,a.w5)((()=>[(0,a.Wm)(u,{circle:"",plain:"",type:"info",onClick:_,size:"large"},{default:(0,a.w5)((()=>[d])),_:1})])),_:1})])),_:1}),(0,a._)("div",p,[m,(0,a.Wm)(i,{to:"/register",style:{color:"rgb(47,110,195)"}},{default:(0,a.w5)((()=>[f])),_:1})])])),_:1})])),_:1})}}},h=l(8696);const w=(0,h.Z)(_,[["__scopeId","data-v-4e11629c"]]);var g=w}}]);