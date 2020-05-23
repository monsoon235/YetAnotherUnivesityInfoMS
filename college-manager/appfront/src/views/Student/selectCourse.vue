<template>
	<div>
        <div style="display: inline-block;float: right;">
            <el-button type="warning" plain @click="dialogFormSearch = true">搜索</el-button>
        </div>
		<div>
			<el-table
            :data="tableData.filter(data => !search || data.name.toLowerCase().includes(search.toLowerCase()))"
          :row-class-name="tableRowClassName"
	      stripe
	      style="width: 100%">
	      <el-table-column
	        prop="course_id"
            sortable
	        label="课程号">
	      </el-table-column>
	      <el-table-column
	        prop="course_name"
            sortable
	        label="课程名">
	      </el-table-column>
          <el-table-column
	        prop="teacher_name"
            sortable
	        label="开课教师">
	      </el-table-column>
          <el-table-column
	        prop="year"
            sortable
	        label="开课学年">
          <template slot-scope="scope">
          {{(scope.row.year==1)?春:秋}}
        </template>
	      </el-table-column>
          <el-table-column
	        prop="term"
            sortable
	        label="开课学期">
	      </el-table-column>
          <el-table-column
	        prop="time"
            sortable
	        label="上课时间">
	      </el-table-column>
	      <el-table-column
	        prop="course_assessment"
            sortable
	        label="考核方式">
	      </el-table-column>
	      <el-table-column
	        prop="course_major_name"
            sortable
	        label="开课专业">
	      </el-table-column>
          <el-table-column
            fixed="right">
            <template slot="header" slot-scope="scope">
                <el-input
                    prefix-icon="el-icon-search"
                    v-model="search"
                    size="mini"
                />
            </template>
            <template slot-scope="scope">
                <el-button v-if="!scope.row.is_selected" @click="addSelection(scope.$index)" type="text" size="small">选中</el-button>
                <el-button v-if="scope.row.is_selected" @click="delSelection(scope.$index)" type="text" size="small">退课</el-button>
            </template>
	      </el-table-column>
	    </el-table>
          <el-dialog title="请填写搜索信息(可只填部分)" :visible.sync="dialogFormSearch" style="height: 100%；">
        <el-form :model="form" :rules="rules" ref="form">
          <el-form-item label="课程号" prop="course_id">
            <el-input v-model="form.course_Id" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="课程名称" prop="course_name">
            <el-input v-model="form.course_name" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="开课专业" prop="course_major_name">
            <el-input v-model="form.course_major_name" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="考核方式" prop="course_assessment">
            <el-input v-model="form.exam_type" autocomplete="off" placeholder="考试或当堂答辩"></el-input>
          </el-form-item>
          <el-form-item label="授课老师" prop="teacher_name">
            <el-input v-model="form.teacher_name" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="开课学年" prop="year">
            <el-input v-model="form.year" autocomplete="off" placeholder="年"></el-input>
          </el-form-item>
          <el-form-item label="开课学期" prop="term">
            <el-select style='width: 100%; position: absolute; left: 138px' v-model="form.term" placeholder="请选择学期">
              <el-option style='height: 80%' label="春" value="春" autocomplete="off"></el-option>
              <el-option style='height: 80%' label="秋" value="秋" autocomplete="off"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="开课时间" prop="time">
            <el-input v-model="form.time" autocomplete="off" placeholder="周一至周五的第一到第九节"></el-input>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="dialogFormSearch = false">取 消</el-button>
          <el-button type="primary" @click="submitSearch">确 定</el-button>
        </div>
      </el-dialog>

	  </div>
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
    .el-table .selected-row{
        background: #f0f8eb;
    }
</style>
<script>
export default {
	name: "index",
	data() {
    return {
    	tableData: [],
      rules: {
      },
      form: {

      },
      search: '',
      dialogFormSearch: false,
    }
  },
  methods: {
		getAllData() {
            var _this = this
            var ldata=[]
	      _this.$http.get('/api/lecture/get').then(function (res) {
	    //   console.log(res)
          ldata = res.data.list
          addSelected(ldata)
	    })
	    .catch(function (error) {
	      console.log(error)
        })
        
      },
      addSelected(ldata){
          var _this = this
          this.$http.post('/api/selection/get').then(function(res){
            var data = res.data.list
            for(var i=0;i<data.length;i++){
                for(var j=0;j<ldata.length;j++){
                    if(data[i].lecture_id==ldata[j].id){
                        ldata[j].is_selected = true
                        _this.tableData.unshift(ldata[j])
                    }else{
                        ldata[j].is_selected = false
                        _this.tableData.push(ldata[j])
                    }
                }

            }
        })
      },
	  searchData() {
	    var _this = this
      console.log(_this.tableData)
      var result = _this.tableData.filter(function(value, index, arr) {
        // console.log(value)
        // console.log(document.getElementsByClassName('sc')[0].value)
        return document.getElementsByClassName('sc')[0].value == value.courseName || document.getElementsByClassName('sc')[0].value == value.courseTime || document.getElementsByClassName('sc')[0].value == value.courseGrade
      })
      // console.log(result)
      _this.tableData = result
    },
    sortUp() {
    	var objectArraySort = function (keyName) {
			 return function (objectN, objectM) {
			  var valueN = objectN[keyName]
			  var valueM = objectM[keyName]
			  if (valueN > valueM) return 1
			  else if (valueN < valueM) return -1
			  else return 0
			 }
			}
    	this.tableData.sort(objectArraySort('courseTime'))
    },
    sortDown() {
    	var objectArraySort = function (keyName) {
			 return function (objectN, objectM) {
			  var valueN = objectN[keyName]
			  var valueM = objectM[keyName]
			  if (valueN < valueM) return 1
			  else if (valueN > valueM) return -1
			  else return 0
			 }
			}
    	this.tableData.sort(objectArraySort('courseTime'))
	 
    },
    tableRowClassName({row,rowIndex}){
        if(this.tableData[rowIndex].is_selected){
            return 'selected-row'
        }else{
            return ''
        }
    },
    addSelection(index){
        var _this = this
        var row = this.tableData[index]
        var data={"lecture_id":row.lecture_id}
        this.$http.post("/api/selection/add",data).then(function(res){
            _this.tableData[index].is_selected=true;
        }).catch(function (error) {
	      console.log(error)
        })
    },
    delSelection(index){
        var _this = this
        var row = _this.tableData[index]
        var data={"lecture_id":row.lecture_id}
        this.$http.post("/api/selection/del",data).then(function (res){
            _this.tableData[index].is_selected=false
        }).catch(function (error) {
            console.log(error)
        })
    },
    submitSearch(){
        var _this = this
        thsi.$http.post("/api/search/get",{params:this.form}).then(function (res){
            _this.tableData=res.data.list
        }).catch(function (error) {
            console.log(error)
        })
    }

  },

  mounted: function() {
    // 组件创建时候去获取所有的用户数据
    this.getAllData();
  }
}
</script>