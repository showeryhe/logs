var formsData = '[{"createdAt":1512652527412,"id":"S1wl1p8WM","formId":"B1V1k6L-M","userId":"test","formData":{"formInfo":[{"type":"header","subtype":"h1","label":"表头"},{"name":"date-1512652499122","className":"form-control","label":"日期字段","type":"date"},{"type":"paragraph","subtype":"p","label":"段落"},{"name":"number-1512652502454","className":"form-control","label":"number","type":"number"},{"name":"radio-group-1512652504190","label":"单选组","type":"radio-group","values":[{"value":"1","label":"选项 1"},{"value":"2","label":"选项 2"},{"value":"3","label":"选项 3"}]},{"name":"textarea-1512652505641","className":"form-control","label":"文本框","type":"textarea","subtype":"textarea"},{"name":"autocomplete-1512652506842","className":"form-control","label":"自动完成","type":"autocomplete","values":[{"value":"1","label":"选项 1"},{"value":"2","label":"选项 2"},{"value":"3","label":"选项 3"}]}],"formData":[{"name":"date-1512652499122","value":"2017-12-08"},{"name":"number-1512652502454","value":"123"},{"name":"radio-group-1512652504190","value":"2"},{"name":"textarea-1512652505641","value":"12123"},{"name":"autocomplete-1512652506842","value":"1"}]}},{"createdAt":1512652572413,"id":"HyVX1aLZM","formId":"B1V1k6L-M","userId":"test","formData":{"formInfo":[{"type":"header","subtype":"h1","label":"表头"},{"name":"date-1512652499122","className":"form-control","label":"日期字段","type":"date"},{"type":"paragraph","subtype":"p","label":"段落"},{"name":"number-1512652502454","className":"form-control","label":"number","type":"number"},{"name":"radio-group-1512652504190","label":"单选组","type":"radio-group","values":[{"value":"1","label":"选项 1"},{"value":"2","label":"选项 2"},{"value":"3","label":"选项 3"}]},{"name":"textarea-1512652505641","className":"form-control","label":"文本框","type":"textarea","subtype":"textarea"},{"name":"autocomplete-1512652506842","className":"form-control","label":"自动完成","type":"autocomplete","values":[{"value":"1","label":"选项 1"},{"value":"2","label":"选项 2"},{"value":"3","label":"选项 3"}]}],"formData":[{"name":"date-1512652499122","value":"2017-12-08"},{"name":"number-1512652502454","value":"234"},{"name":"radio-group-1512652504190","value":"2"},{"name":"textarea-1512652505641","value":"234"},{"name":"autocomplete-1512652506842","value":"42"}]}}]'

$(document).ready(function () {
  var parsedFormsData = JSON.parse(formsData);
  var dataSet = [];
  var columns = [];
  for (var i = 0; i < parsedFormsData.length; i++) {
    var formData = parsedFormsData[i].formData.formData;
    var formArray = [];
    for (var j = 0; j < formData.length; j++) {
      formArray.push(formData[j].value)
    }
    dataSet.push(formArray)
  }
  let formInfo = parsedFormsData[0].formData.formInfo;
  for (var i = 0; i < formInfo.length; i++) {
    var fieldInfo = formInfo[i];
    console.log(fieldInfo.type)
    if (fieldInfo.type !== 'header' && fieldInfo.type !== 'hidden' && fieldInfo.type !== 'paragraph') {
      columns.push({
        title: fieldInfo.label
      })
    }
  }
  console.log(dataSet, columns)
  $('#results').DataTable({
    "language": {
      "url": "https://cdn.datatables.net/plug-ins/1.10.16/i18n/Chinese.json"
    },
    dom: 'Bfrtip',
    buttons: [
      'copy', 'csv', 'excel', 'print'
    ],
    data: dataSet,
    columns: columns
  });
});
