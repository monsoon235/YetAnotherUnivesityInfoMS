import Vue from 'vue'
import Router from 'vue-router'

// import Test from '@/views/Test.vue'
import Register from '@/views/Register.vue'
import Login from '@/views/Login.vue'
import Main from '@/views/Main.vue'
import Manager from '@/views/Manager.vue'
import Teacher from '@/views/Teacher.vue'
import Student from '@/views/Student.vue'

import start from '@/views/Manager/start.vue'
import userManage from '@/views/Manager/userManage.vue'
import teacherMsgManage from '@/views/Manager/teacherMsgManage.vue'
import classMsgManager from '@/views/Manager/classMsgManager.vue'
import studentMsgMange from '@/views/Manager/studentMsgMange.vue'

import campusManager from '@/views/Manager/campusManager.vue'
import majorManager from '@/views/Manager/majorManager.vue'
import adjustmentManager from '@/views/Manager/adjustmentManager.vue'
import lectureManager from '@/views/Manager/lectureManager.vue'
import selectionManager from '@/views/Manager/selectionManager.vue'
import courseManager from '@/views/Manager/courseManager.vue'


// import HelloWorld from '@/components/HelloWorld'

import teaStart from '@/views/Teacher/start.vue'
import teaMessage from '@/views/Teacher/teaMessage.vue'
import startCourse from '@/views/Teacher/startCourse.vue'


import stuSelectCourse from '@/views/Student/selectCourse.vue'
import stuMessage from '@/views/Student/stuMessage.vue'
import stuClassMessage from '@/views/Student/classMessage.vue'



Vue.use(Router)

export default new Router({
  routes : [
  // { path: '/test', name: 'Test', component: Test },
  { path: '/login', name: 'Login', component: Login },
  { path: '/register', name: 'Register', component: Register },
  { path: '/main', name: 'Main', component: Main },
  {
    path: '/manager',
    name: 'Manager',
    component: Manager,
    children: [

      { path: 'userManage', component: userManage },
      { path: 'campusManager', component: campusManager },
      { path: 'majorManager', component: majorManager },
      { path: 'adjustmentManager', component: adjustmentManager },

      { path: 'studentMsgMange', component: studentMsgMange },

      { path: 'courseManager', component: courseManager },
      { path: 'lectureManager', component: lectureManager },
      { path: 'selectionManager', component: selectionManager },
      { path: 'classMsgManager', component: classMsgManager },

      { path: 'teacherMsgManage', component: teacherMsgManage },
      { path: '*', component: start },

    ]
  },


  { path:
    '/teacher',
    name: 'Teacher',
    component: Teacher,
    children: [
      { path: 'teaMessage', component: teaMessage},
      { path: 'startCourse', component: startCourse },
      { path: '*', component: teaStart }
    ]
  },
  { path:
    '/student',
    name: 'Student',
    component: Student,
    children: [
      { path: 'stuMessage', component: stuMessage},
      { path: 'classMessage', component: stuClassMessage},
      { path: 'selectCourse', component: stuSelectCourse},
      { path: '*', component: stuMessage },

    ]
  },
  { path: '*', name: 'Login', component: Login }
]
})
