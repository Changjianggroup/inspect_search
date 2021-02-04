<template>
  <div id="app">
    <el-container>
    <el-header height="60px"><h1>基础运维平台审计查询</h1></el-header>
      <el-form :inline="true" class="date_search">
        <el-form-item label="审计开始日期：">
        <el-date-picker
        v-model="value_date_begin"
        value-format="yyyy-MM-dd"
        type="date"
        placeholder="选择日期时间"
        align="right"
        format="yyyy-MM-dd"
        :picker-options="pickerOptions">
    </el-date-picker>
        </el-form-item>
        <el-form-item label="审计结束日期：" >
    <el-date-picker
        v-model="value_date_end"
        value-format="yyyy-MM-dd"
        type="date"
        placeholder="选择日期时间"
        align="right"
        format="yyyy-MM-dd"
        :picker-options="pickerOptions">
    </el-date-picker>
        </el-form-item>
        <el-form-item >
          <el-button type="success" round @click="handleSearchInspectInfo">查询</el-button>
          <el-button type="info" round @click="handleResetSearch">重置</el-button>
        </el-form-item>
      </el-form>
      </el-container>
    <el-row :gutter="10" class="mb8">
      <el-col :span="1.5">
        <el-button
            type="warning"
            icon="el-icon-download"
            size="mini"
            @click="handleExport"
        >导出</el-button>
      </el-col>
    </el-row>
    <info-list ref="inspectListTable" :values="inspect_list"  ></info-list>
    <el-row class="bottom-class">
      <el-col :span="8" :offset="6">
        <div class="pagination">
          <el-pagination
              :page-sizes="[5, 10, 100, 200]"
              :page-size="queryParams.page_size"
              :total="totalNum"
              layout="total, sizes, prev, pager, next"
              @size-change="handleSizeChange"
              @current-change="handleCurrentChange">
<!--              :current-page.sync="queryParams.page">-->
          </el-pagination>
        </div>
      </el-col>
    </el-row>
  </div>

</template>

<script>
import { getInspectInfoList } from '@/api/inspect'
import InfoList from '@/components/list'
import { formatJson } from '@/utils'
export default {
  name: 'App',
  components: { InfoList },
  data (){
    return {
      pickerOptions: {
        shortcuts: [{
          text: '今天',
          onClick(picker) {
            picker.$emit('pick', new Date());
          }
        }, {
          text: '昨天',
          onClick(picker) {
            const date = new Date();
            date.setTime(date.getTime() - 3600 * 1000 * 24);
            picker.$emit('pick', date);
          }
        }, {
          text: '一周前',
          onClick(picker) {
            const date = new Date();
            date.setTime(date.getTime() - 3600 * 1000 * 24 * 7);
            picker.$emit('pick', date);
          }
        }]
      },
      value_date_begin: '',
      value_date_end: '',
      inspect_list: [],
      totalNum: 0,
      queryParams: {
        page: 1,
        page_size: 5,
        begin: '',
        end: '',
      },
    }
  },
  created() {
   this.fetchData()
  },
  methods: {
    fetchData() {
      getInspectInfoList(this.queryParams).then(
          // 系统审计信息列表
          res => {
            this.inspect_list = res.data
            this.totalNum = res.count
          },
          err => {
            this.$message({
              type: 'error',
              message: err
            })
          }
      )
    },
    handleSearchInspectInfo() {
      this.queryParams.begin = this.value_date_begin
      this.queryParams.end = this.value_date_end
      this.fetchData()
    },
    handleResetSearch() {
      this.queryParams.begin = ''
      this.queryParams.end = ''
      this.value_date_end = ''
      this.value_date_begin = ''
    },
    handleCurrentChange(val) {
      // 分页
      this.queryParams.page = val
      this.fetchData()
    },
    handleSizeChange(val) {
      // 改变分页大小
      this.queryParams.page_size = val
      this.fetchData()
    },
    handleExport() {
      // const queryParams = this.queryParams
      this.$confirm('是否确认导出审计数据表单?', '警告', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.downloadLoading = true
        import('@/utils/Export2Excel').then(excel => {
          const tHeader = ['审计时间', '审计系统','系统owner', '审计内容', '审计人员', '异常情况']
          const filterVal = ['date', 'app_name','app_owner', 'content', 'operator', 'abnormal_result']
          const data = formatJson(filterVal, this.inspect_list)
          excel.export_json_to_excel({
            header: tHeader,
            data,
            filename: '基础平台审计日志',
            autoWidth: true, // Optional
            bookType: 'xlsx' // Optional
          })
          this.downloadLoading = false
        })
      })
    }
 }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 10px;
}
</style>
