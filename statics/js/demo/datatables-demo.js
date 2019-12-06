// // Call the dataTables jQuery plugin
// $(document).ready(function () {
//   $('#dataTable').DataTable({
//     "language": {
//       "sProcessing": "Procesando...",
//       "sLengthMenu": "Mostrar _MENU_ registros",
//       "sZeroRecords": "No se encontraron resultados",
//       "sEmptyTable": "Ningún dato disponible en esta tabla =(",
//       "sInfo": "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
//       "sInfoEmpty": "Mostrando registros del 0 al 0 de un total de 0 registros",
//       "sInfoFiltered": "(filtrado de un total de _MAX_ registros)",
//       "sInfoPostFix": "",
//       "sSearch": "Buscar:",
//       "sUrl": "",
//       "sInfoThousands": ",",
//       "sLoadingRecords": "Cargando...",
//       "oPaginate": {
//         "sFirst": "<<",
//         "sLast": ">>",
//         "sNext": ">",
//         "sPrevious": "<"
//       },
//       "oAria": {
//         "sSortAscending": ": Activar para ordenar la columna de manera ascendente",
//         "sSortDescending": ": Activar para ordenar la columna de manera descendente"
//       },
//       "buttons": {
//         "copy": "Copiar",
//         "colvis": "Visibilidad"
//       }
//     }
//   });
// });

$(document).ready(function() {
  $('#dataTable').DataTable( {
    
      initComplete: function () {
        
          this.api().columns([0,1,2,3,4,5,6]).every( function () {
              var column = this;
              var select = $('<select><option value=""></option></select>')
                  .appendTo( $(column.footer()).empty() )
                  .on( 'change', function () {
                      var val = $.fn.dataTable.util.escapeRegex(
                          $(this).val()
                      );

                      column
                          .search( val ? '^'+val+'$' : '', true, false )
                          .draw();
                  } );

              column.data().unique().sort().each( function ( d, j ) {
                  select.append( '<option value="'+d+'">'+d+'</option>' )
              } );
          } );
      },
      "language": {
        "sProcessing": "Procesando...",
        "sLengthMenu": "Mostrar _MENU_ registros",
        "sZeroRecords": "No se encontraron resultados",
        "sEmptyTable": "Ningún dato disponible en esta tabla =(",
        "sInfo": "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
        "sInfoEmpty": "Mostrando registros del 0 al 0 de un total de 0 registros",
        "sInfoFiltered": "(filtrado de un total de _MAX_ registros)",
        "sInfoPostFix": "",
        "sSearch": "Buscar:",
        "sUrl": "",
        "sInfoThousands": ",",
        "sLoadingRecords": "Cargando...",
        "oPaginate": {
          "sFirst": "<<",
          "sLast": ">>",
          "sNext": ">",
          "sPrevious": "<"
        },
        "oAria": {
          "sSortAscending": ": Activar para ordenar la columna de manera ascendente",
          "sSortDescending": ": Activar para ordenar la columna de manera descendente"
        },
        "buttons": {
          "copy": "Copiar",
          "colvis": "Visibilidad"
        }
      }
  }
   );
} );