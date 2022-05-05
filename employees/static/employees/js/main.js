$(document).ready(function () {
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
      data: JSON.stringify({ is_completed: this.checked }),
      success: function (response, textStatus, jqXhr) {
        console.log("Udało się!!!");
      },
      error: function (response, textStatus, jqXhr) {
        console.log("Nie udało się...");
      },
    });
  });
});
