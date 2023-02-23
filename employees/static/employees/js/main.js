$(document).ready(function () {
    const taskFullList = get_task_data();

    function get_task_data() {
        let task_list = [];
        const task_table = $(".task");
        for (row of task_table) {
            task_list.push({
                is_checked: $(row).find(".task-completed-checkbox")[0].checked,
                description: $(row).find(".task-description")[0].innerText,
                status: $(row).find(".task-status")[0].innerText,
                category: $(row).find(".task-category")[0].innerText,
                dueDate: $(row).find(".task-end-date")[0].innerText,
                taskId: $(row).find(".task-completed-checkbox")[0].id,
                counter: $(".delete-confirm")[0].id,
            });
        }
        return task_list;
    }

    function draw_task_data(task_data) {
        const task_table = $(".task-container").empty();
        if (task_data) {
            for (row of task_data) {
                $(task_table).append(`<tr class="task">
        <th scope="row">
          <input
            type="checkbox"
            name="task-completed-${row.taskId}"
            class="task-completed-checkbox"
            id="${row.taskId}"
            ${row.is_checked ? "checked" : ""}
          >
        </th>
        <td class="task-description">${row.description}</td>
        <td class="task-status">${row.status}</td>
        <td class="task-category">${row.category}</td>
        <td class="task-end-date">
        ${row.dueDate}
        </td>
        <td>
          <button
            type="button"
            class="btn btn-danger btn-sm"
            data-toggle="modal"
            data-target="#confirmModal${row.counter}"
          >
            Usuń
          </button>
        </td>
      </tr>`);
            }
        } else {
            $(task_table).append(`<tr>
      <td colspan="4">
        <p>Nie znaleziono tasków</p>
      </td>
    </tr>`);
        }
    }

    function applyFilters() {
        let taskSnapshot = taskFullList;
        const dateFilter = $(".date-filter")[0];
        const statusFilter = $(".status-filter")[0];

        if ($(statusFilter).find(".status-checkbox")[0].checked) {
            const status = $(statusFilter).find("#status-select")[0].value;
            if (status) {
                taskSnapshot = taskSnapshot.filter((task) => {
                    return task.status === status;
                });
            }
        }

        if ($(dateFilter).find(".date-checkbox")[0].checked) {
            let startDate = $(dateFilter).find("input[name='from-day']")[0].value;
            let endDate = $(dateFilter).find("input[name='to-day']")[0].value;
            // startDate = new Date(startDate.split("-"));
            // endDate = new Date(endDate.split("-"));
            // startDate.setHours(0, 0, 0, 0);
            // endDate.setHours(0, 0, 0, 0);
            // console.log(
            //   `Dates filter: ${startDate.getTime()} - ${endDate.getTime()}, ${
            //     startDate.getTime() === endDate.getTime()
            //   }`
            // );
            // console.log(`Task Date: ${new Date(taskSnapshot[0].dueDate.split("-"))}`);
            if (startDate && endDate) {
                startDate = new Date(startDate.split("-"));
                endDate = new Date(endDate.split("-"));
                startDate.setHours(0, 0, 0, 0);
                endDate.setHours(0, 0, 0, 0);
                if (startDate.getTime() > endDate.getTime()) {
                    startDate = endDate;
                }
                taskSnapshot = taskSnapshot.filter((task) => {
                    let task_date = new Date(task.dueDate.split("-"));
                    task_date.setHours(0, 0, 0, 0);
                    console.log(
                        task_date.getTime(),
                        startDate.getTime(),
                        endDate.getTime()
                    );
                    return (
                        task_date.getTime() >= startDate.getTime() &&
                        task_date.getTime() <= endDate.getTime()
                    );
                });
                console.log(taskSnapshot);
            }
        }

        draw_task_data(taskSnapshot);
    }

    $(".filter-checkbox").on("change", applyFilters);
    $("#status-select").on("change", applyFilters);
    $("input[type='date']").on("change", applyFilters);

    $(".clickable-row").click(function () {
        window.location = $(this).data("href");
    });

    $(".task-completed").on("change", function () {
        const task_id = this.id;
        $.ajax({
            headers: {
                "content-type": "application/json",
            },
            url: `http://localhost:8000/api/v1.0/tasks/${task_id}/update/`,
            type: "PATCH",
            data: JSON.stringify({is_completed: this.checked}),
            success: function (response, textStatus, jqXhr) {
                console.log("Udało się!!!");
            },
            error: function (response, textStatus, jqXhr) {
                console.log("Nie udało się...");
            },
        });
    });

    function prepareModalForm() {
        console.log("prepareModalForm");
        $('#modalForm').submit(function (e) {
            e.preventDefault();
            var modal = $('#createModal')
            $.ajax({
                url: $('#modalForm').attr('action'),
                type: 'POST',
                data: $('#modalForm').serialize(),
                success: function (xhr, ajaxOptions, thrownError) {

                    $(modal).find('.modal-body').html(xhr);

                    if ($(xhr).find('.invalid-feedback, .errorlist').length === 0) {
                        {
                            $(modal).modal('hide');
                            window.location.reload(true);
                        }
                    } else {
                        prepareModalForm()
                    }
                }
            });
            return false;
        });
    }
    prepareModalForm();
});
