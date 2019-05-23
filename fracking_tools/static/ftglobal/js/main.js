function checkTaskStatus(taskUrl, taskData) {
    $.ajax({
        url: taskUrl,
        data: {'task-id': taskData},
        dataType: 'json',
        success: statusCheck
    }); 
}

function statusCheck(data) {
    if (data.status == 'SUCCESS') {
        // Stop checking for task status
        clearInterval(intervalId); 

        // Set task-status and build button to show results are available
        $('.task-status').text(successMessage);             
        $('#run-btn').html(
            `<button type="submit" class="btn btn-dark btn-block disabled" name="button" disabled> 
                Finished <i class="fas fa-check"></i>
            </button>`
        );

        // Download results 
        downloadResults(downloadUrl); 
        
        // Tell user file has been downloaded
        $('.task-status').text(downloadMessage);

        setTimeout(function() {
            resetWindow(windowHomeUrl); 
        }, 5000); 
    } else if (data.status == 'FAILURE') {
        $('.task-status').text(data.traceback);             
        $('#run-btn').html(
            `<button type="submit" class="btn btn-dark btn-block disabled" name="button" disabled> 
                Failed <i class="fa fa-exclamation-triangle"></i>
            </button>`
        );
    }
}

function resetWindow(windowHomeUrl) {
    window.location.replace(windowHomeUrl);
}


function downloadResults(downloadUrl) {
    window.location.replace(downloadUrl);
}
