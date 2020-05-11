<template>
  <div class="home">
    <el-row display="margin-top:10px">
        <el-input v-model="input" placeholder="请输入学生姓名" style="display:inline-table; width: 30%; float:left"></el-input>
        <el-button type="primary" @click="addStudent()" style="float:left; margin: 2px;">新增</el-button>
    </el-row>
    <el-row>
        <el-table :data="studentList" style="width: 100%" border>
          <el-table-column prop="id" label="编号" min-width="100">
            <template slot-scope="scope"> {{ scope.row.pk }} </template>
          </el-table-column>
          <el-table-column prop="student_name" label="学生姓名" min-width="100">
            <template slot-scope="scope"> {{ scope.row.fields.student_name }} </template>
          </el-table-column>
          <el-table-column prop="add_time" label="添加时间" min-width="100">
            <template slot-scope="scope"> {{ scope.row.fields.add_time }} </template>
          </el-table-column>
        </el-table>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'home',
  data () {
    return {
      input: '',
      studentList: []
    }
  },
  mounted: function () {
    this.showStudents()
  },
  methods: {
    addStudent () {
      this.$http.get('http://127.0.0.1:8000/api/add_student?student_name=' + this.input)
        .then((response) => {
          var res = JSON.parse(response.bodyText)
          if (res.error_num === 0) {
            this.showStudents()
          } else {
            this.$message.error('新增学生失败，请重试')
            console.log(res['msg'])
          }
        })
    },
    showStudents () {
      this.$http.get('http://127.0.0.1:8000/api/show_students')
        .then((response) => {
          var res = JSON.parse(response.bodyText)
          console.log(res)
          if (res.error_num === 0) {
            this.studentList = res['list']
          } else {
            this.$message.error('查询学生失败')
            console.log(res['msg'])
          }
        })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  h1, h2 {
    font-weight: normal;
  }

  ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
