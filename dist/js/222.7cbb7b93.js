"use strict";(self["webpackChunkcs2305_his"]=self["webpackChunkcs2305_his"]||[]).push([[222],{4222:function(e,l,a){a.r(l),a.d(l,{default:function(){return U}});a(4119);var t=a(7279),u=a(7313),o=a(1481),n=a(5448),i=a(3247),d=a(6043);const s={class:"dialog-footer"},m={key:0},r=(0,t.Uk)("取消"),c=(0,t.Uk)(" 添加 "),p={key:1},v=(0,t.Uk)("取消"),w=(0,t.Uk)(" 修改 "),f=(0,t.Uk)(" 删除 "),g=(0,t.Uk)("刷新"),y=(0,t.Uk)("添加");var k={name:"DataRaw",setup(e){const l=(0,u.iH)([]),a=(0,n.oR)().state.columns,k=JSON.parse((0,i.yj)().query.item),b=k.dataColumns,U=k.table,_=k.pk,V=k.dateCol,W=k.datetimeCol,C=[_],D=async()=>{const e=await o.Z.getAllData(U);l.value=e.data.content,console.log(l.value)};(0,t.bv)(D);const S=(0,u.iH)(!1),h=(0,u.iH)({}),j=(0,u.iH)(!1);let H={};const M=e=>{j.value=!1,h.value={...e},H={...e},S.value=!0},T=e=>{if(V.includes(e)){let l=new Date(h.value[e]);l-=6e4*l.getTimezoneOffset(),h.value[e]=new Date(l).toISOString().slice(0,10)}else if(W.includes(e)){let l=new Date(h.value[e]);l-=6e4*l.getTimezoneOffset(),h.value[e]=new Date(l).toISOString().slice(0,19).replace("T"," ")}},O=async()=>{for(let e in h.value)if(h.value[e]!=H[e]){T(e);const l=await o.Z.update(U,h.value[_],e,h.value[e],_);console.log(l.data),!1===l.data.error?(0,d.bM)({title:"提交失败",message:l.data.content}):(0,d.bM)({title:"提交成功"}),console.log([U,h.value[_],e,h.value[e],_])}S.value=!1,setTimeout(D,500)},x=async()=>{const e=await o.Z["delete"](U,h.value[_],_);!1===e.data.error?(0,d.bM)({title:"提交失败",message:e.data.content}):(0,d.bM)({title:"提交成功"}),S.value=!1,setTimeout(D,500)},Z=async()=>{let e=[];for(let a in h.value)T(a),e.push(h.value[a]);const l=await o.Z.insert(U,e);!1===l.data.error?(0,d.bM)({title:"提交失败",message:l.data.content}):(0,d.bM)({title:"提交成功"}),S.value=!1,setTimeout(D,500)},R=()=>{j.value=!0,S.value=!0,h.value={}};return(e,o)=>{const n=(0,t.up)("el-date-picker"),i=(0,t.up)("el-input"),d=(0,t.up)("el-form-item"),k=(0,t.up)("el-form"),U=(0,t.up)("el-button"),_=(0,t.up)("el-dialog"),H=(0,t.up)("el-table-column"),T=(0,t.up)("el-table"),Y=(0,t.up)("el-main"),z=(0,t.up)("el-row"),I=(0,t.up)("el-footer");return(0,t.wg)(),(0,t.iD)(t.HY,null,[(0,t.Wm)(_,{modelValue:S.value,"onUpdate:modelValue":o[2]||(o[2]=e=>S.value=e),title:"编辑",draggable:"",style:{"max-width":"fit-content"},"label-position":"right"},{footer:(0,t.w5)((()=>[(0,t._)("span",s,[j.value?((0,t.wg)(),(0,t.iD)("div",m,[(0,t.Wm)(U,{onClick:o[0]||(o[0]=e=>S.value=!1)},{default:(0,t.w5)((()=>[r])),_:1}),(0,t.Wm)(U,{type:"primary",onClick:Z},{default:(0,t.w5)((()=>[c])),_:1})])):((0,t.wg)(),(0,t.iD)("div",p,[(0,t.Wm)(U,{onClick:o[1]||(o[1]=e=>S.value=!1)},{default:(0,t.w5)((()=>[v])),_:1}),(0,t.Wm)(U,{type:"primary",onClick:O},{default:(0,t.w5)((()=>[w])),_:1}),(0,t.Wm)(U,{type:"primary",onClick:x},{default:(0,t.w5)((()=>[f])),_:1})]))])])),default:(0,t.w5)((()=>[(0,t.Wm)(k,null,{default:(0,t.w5)((()=>[((0,t.wg)(!0),(0,t.iD)(t.HY,null,(0,t.Ko)((0,u.SU)(b),(e=>((0,t.wg)(),(0,t.j4)(d,{key:e,prop:e,label:(0,u.SU)(a).get(e)},{default:(0,t.w5)((()=>[(0,u.SU)(V).includes(e)?((0,t.wg)(),(0,t.j4)(n,{key:0,modelValue:h.value[e],"onUpdate:modelValue":l=>h.value[e]=l,disabled:!j.value&&C.includes(e),type:"date"},null,8,["modelValue","onUpdate:modelValue","disabled"])):(0,u.SU)(W).includes(e)?((0,t.wg)(),(0,t.j4)(n,{key:1,modelValue:h.value[e],"onUpdate:modelValue":l=>h.value[e]=l,disabled:!j.value&&C.includes(e),type:"datetime"},null,8,["modelValue","onUpdate:modelValue","disabled"])):((0,t.wg)(),(0,t.j4)(i,{key:2,modelValue:h.value[e],"onUpdate:modelValue":l=>h.value[e]=l,disabled:!j.value&&C.includes(e)},null,8,["modelValue","onUpdate:modelValue","disabled"]))])),_:2},1032,["prop","label"])))),128))])),_:1})])),_:1},8,["modelValue"]),(0,t.Wm)(Y,null,{default:(0,t.w5)((()=>[(0,t.Wm)(T,{data:l.value,onRowClick:M,border:"","max-height":"600"},{default:(0,t.w5)((()=>[(0,t.Wm)(H,{type:"index"}),((0,t.wg)(!0),(0,t.iD)(t.HY,null,(0,t.Ko)((0,u.SU)(b),(e=>((0,t.wg)(),(0,t.j4)(H,{key:e,prop:e,label:(0,u.SU)(a).get(e)},null,8,["prop","label"])))),128))])),_:1},8,["data"])])),_:1}),(0,t.Wm)(I,null,{default:(0,t.w5)((()=>[(0,t.Wm)(z,{style:{"{align-items":"center","justify-content":"center",display:"flex"}},{default:(0,t.w5)((()=>[(0,t.Wm)(U,{type:"primary",onClick:D},{default:(0,t.w5)((()=>[g])),_:1}),(0,t.Wm)(U,{type:"primary",onClick:R},{default:(0,t.w5)((()=>[y])),_:1})])),_:1})])),_:1})],64)}}};const b=k;var U=b}}]);