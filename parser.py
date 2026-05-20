def parse_logs(file_path):
    log_data = {
        "INFO": [],
        "WARNING": [],
        "ERROR": []
    }

    error_counts = {}

    with open(file_path, "r") as file:
        for line in file:
            clean_line = line.strip()

            if "INFO" in clean_line:
                log_data["INFO"].append(clean_line)

            elif "WARNING" in clean_line:
                log_data["WARNING"].append(clean_line)

            elif "ERROR" in clean_line:
                log_data["ERROR"].append(clean_line)

                error_message = clean_line.replace("ERROR ", "")

                if error_message in error_counts:
                    error_counts[error_message] += 1
                else:
                    error_counts[error_message] = 1

    return log_data, error_counts
