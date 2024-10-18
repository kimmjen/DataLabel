<script setup>

import {ref} from "vue";
import axios from 'axios';

const model = ref("");
// const rows = ref([]);
//
// // 테이블의 컬럼 정의
// const columns = ref([
//   { name: 'id', label: 'ID', field: 'id', align: 'left' },
//   { name: 'name', label: 'Name', field: 'name', align: 'left' },
//   { name: 'age', label: 'Age', field: 'age', align: 'left' },
//   { name: 'gender', label: 'Gender', field: 'gender', align: 'left' },
//   { name: 'email', label: 'Email', field: 'email', align: 'left' },
//   { name: 'join_date', label: 'Join Date', field: 'join_date', align: 'left' },
//   { name: 'salary', label: 'Salary', field: 'salary', align: 'right' },
//   { name: 'department', label: 'Department', field: 'department', align: 'left' }
// ]);

const rows = ref([]);
const columns = ref([]);
const filename = ref(null)


const loading = ref(false);
const progress = ref(false)

// 파일 제출 함수 (실제 서버로 파일 업로드)
function submit() {
  if (model.value) {
    loading.value = true;  // 업로드 시작 시 로딩 상태 설정
    const formData = new FormData();
    formData.append('file', model.value);

    axios.post('http://localhost:8000/api/uploadfile', formData)
        .then((res) => {
          // 서버로부터 받은 데이터 설정
          filename.value = res.data.filename
          const data_ = res.data.data
          // 'data' 필드가 배열인지 확인하고 배열로 변환
          if (Array.isArray(data_)) {
            rows.value = data_.data;  // 배열일 경우 그대로 설정
          } else {
            rows.value = Object.values(data_.data);  // 객체일 경우 배열로 변환
          }
          const fields = data_.schema.fields
          // 열 설정 (데이터의 첫 번째 행을 기반으로 열 정보 설정)
          columns.value = fields.map(field => ({
            name: field.name,
            label: field.name.charAt(0).toUpperCase() + field.name.slice(1),  // 첫 글자 대문자
            field: field.name,
            align: 'left'  // 기본 정렬 설정
          }));


          loading.value = false;  // 로딩 상태 종료
          alert('파일 업로드 성공');
        })
        .catch((error) => {
          loading.value = false;
          console.error("파일 업로드 실패:", error);
          alert('파일 업로드 실패');
        });
  } else {
    alert('파일을 선택해주세요.');
  }
}
</script>

<template>
  <div class="flex">
    <q-file filled bottom-slots v-model="model" label="Label" counter>
      <template v-slot:prepend>
        <q-icon name="cloud_upload" @click.stop.prevent/>
      </template>
      <template v-slot:append>
        <q-icon name="close" @click.stop.prevent="model = null" class="cursor-pointer"/>
      </template>

      <template v-slot:hint>
        Field hint
      </template>
    </q-file>
    <div class="flex items-center">
      <div class="row">
        <q-btn size="sm" :loading="loading" color="secondary" @click="submit" label="Button"/>
      </div>
    </div>
  </div>
  <div class="flex">
    <div class="row">
      <q-page class="q-pa-md">
        <q-table
            :rows="rows"
            :columns="columns"
            row-key="id"
            :title="filename ? filename : '업로드된 파일'"/>
      </q-page>
    </div>
    <div class="row">
      <q-page class="q-pa-md">
        <q-table
            :rows="rows"
            :columns="columns"
            row-key="id"
            :title="filename ? filename : '업로드된 파일'"/>
      </q-page>
    </div>
  </div>
</template>

<style scoped>

</style>