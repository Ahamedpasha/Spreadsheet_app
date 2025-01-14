$(document).ready(() => {
    fetchData();

    // Fetch and populate data
    function fetchData() {
        $.get("/get_data", (data) => {
            let table = $("#spreadsheet tbody");
            table.empty();

            for (let row in data) {
                let tr = `<tr><td>${row}</td>`;
                for (let col in data[row]) {
                    tr += `<td contenteditable="true" 
                               data-row="${row}" 
                               data-col="${col}">
                               ${data[row][col]}</td>`;
                }
                tr += "</tr>";
                table.append(tr);
            }

            // Update cell on blur
            $("#spreadsheet td[contenteditable=true]").blur(function () {
                let row = $(this).data("row");
                let col = $(this).data("col");
                let value = $(this).text();
                updateCell(row, col, value);
            });
        });
    }

    function updateCell(row, col, value) {
        $.post("/update_cell", { row, col, value });
    }

    window.applyFunction = function (func) {
        let col = prompt("Enter column name:");
        $.post(
            "/apply_function",
            { function: func, col },
            (response) => alert(response.result)
        );
    };

    window.findAndReplace = function () {
        let find = prompt("Find:");
        let replace = prompt("Replace:");
        $.post("/apply_function", { function: "FIND_AND_REPLACE", find, replace }, (response) =>
            alert(response.result)
        );
    };
});
