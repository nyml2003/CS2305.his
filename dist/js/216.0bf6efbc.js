"use strict";(self["webpackChunkcs2305_his"]=self["webpackChunkcs2305_his"]||[]).push([[216],{5216:function(e,t,l){l.r(t),l.d(t,{default:function(){return d}});var a=l(7279),n=l(7313),u=l(1481),s=l(5448),o=l(3247);const i=(0,a.Uk)("刷新");var c={name:"DataView",setup(e){const t=(0,n.iH)([]),l=(0,s.oR)().state.columns,c=JSON.parse((0,o.yj)().query.item),r=c.dataColumns,d=c.view,f=c.dateCol,p=c.datetimeCol,w=async()=>{const e=await u.Z.getView(d);e.data.status&&console.log(e.data.status),t.value=e.data.content,console.log(t.value);for(let t in m.value)g(t)};(0,a.bv)(w);const m=(0,n.iH)({}),g=e=>{if(f.includes(e)){let t=new Date(m.value[e]);t-=6e4*t.getTimezoneOffset(),m.value[e]=new Date(t).toISOString().slice(0,10)}else if(p.includes(e)){let t=new Date(m.value[e]);t-=6e4*t.getTimezoneOffset(),m.value[e]=new Date(t).toISOString().slice(0,19).replace("T"," ")}};return(e,u)=>{const s=(0,a.up)("el-table-column"),o=(0,a.up)("el-table"),c=(0,a.up)("el-main"),d=(0,a.up)("el-button"),f=(0,a.up)("el-row"),p=(0,a.up)("el-footer");return(0,a.wg)(),(0,a.iD)(a.HY,null,[(0,a.Wm)(c,null,{default:(0,a.w5)((()=>[(0,a.Wm)(o,{data:t.value,border:"","max-height":"600"},{default:(0,a.w5)((()=>[(0,a.Wm)(s,{type:"index"}),((0,a.wg)(!0),(0,a.iD)(a.HY,null,(0,a.Ko)((0,n.SU)(r),(e=>((0,a.wg)(),(0,a.j4)(s,{key:e,prop:e,label:(0,n.SU)(l).get(e)},null,8,["prop","label"])))),128))])),_:1},8,["data"])])),_:1}),(0,a.Wm)(p,null,{default:(0,a.w5)((()=>[(0,a.Wm)(f,{style:{"{align-items":"center","justify-content":"center",display:"flex"}},{default:(0,a.w5)((()=>[(0,a.Wm)(d,{type:"primary",onClick:w},{default:(0,a.w5)((()=>[i])),_:1})])),_:1})])),_:1})],64)}}};const r=c;var d=r}}]);