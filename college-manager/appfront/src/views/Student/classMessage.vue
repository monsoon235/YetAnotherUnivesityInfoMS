<template>
  <div>
    <el-row>
      <span class="font">以下是您所在班级的信息</span>
      <div class="searchbox" style="display: inline-block; float: right;">
        <el-button type="danger" plain @click="getAllData()">刷新</el-button>
      </div>
	  </el-row>
		<el-table
      :data="tableData"
      stripe
      style="width: 100%; height: 100%">
      <!-- <el-table-column
        prop="className"
        label="班级名">
      </el-table-column> -->
      <!-- <el-table-column
        prop="stage"
        label="适应阶段">
      </el-table-column> -->
      <el-table-column
        prop="id"
        label="班级编号">
      </el-table-column>
      <el-table-column
        prop="name"
        label="班级名">
      </el-table-column>
      <el-table-column
        prop="found_date"
        label="创班日期">
      </el-table-column>
      <el-table-column
        prop="grade"
        label="年级">
      </el-table-column>
      <el-table-column
        prop="charge_teacher_name"
        label="班主任">
      </el-table-column>
      <el-table-column
        prop="major_name"
        label="专业">
      </el-table-column>
    </el-table>
  </div>
</template>
<style lang='scss'>
  @import "../../static/css/base.scss";
  .font {
    @include fontTwo()
  }
  .text {
		@include fontThree()

	}

</style>
<script>
export default {
	name: "index",
	data() {
    return {
      tableData: [],
      form: {
      	id: '',
      	name: '',
        found_date: '',
        grade: null,
        major_name: '',
        charge_teacher_name: '',
      },
      cls: [],
      rules: {
      }
    }
  },
methods: {
		// 获取所有的用户信息
	getAllData() {
		var _this = this
      this.$http.get('/api/student/get').then(function (res) {
      	// console.log(res);
        _this.$http.post('/api/class/get', {class_id: res.data.list.class_id}).then(function (res) {
          console.log(res)
          if(res.data.list.length === 0||res.data.code==0) {
            console.log(res.data.msg)
            alert('Sorry, 还没有您的班级信息，请联系教学管理者');
            return
          }
          _this.tableData = res.data.list
        })
        .catch(function (error) {
          console.log(error)
        })
      })
      this.$http.post("http://127.0.0.1:8000/api/test",{where:{"id":"1"}})
  
  },
  },	
  mounted: function() {
    // 组件创建时候去获取所有的用户数据
    this.getAllData();
	},
}
</script>
