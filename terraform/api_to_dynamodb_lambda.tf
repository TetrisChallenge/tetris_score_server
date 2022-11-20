data "archive_file" "api_to_dynamodb_function_source" {
  type        = "zip"
  source_dir  = var.get_result_from_dynamodb_function_src_dir
  output_path = var.get_result_from_dynamodb_function_zip_output_path
}

data "archive_file" "api_to_dynamodb_layer_zip" {
  type        = "zip"
  source_dir  = var.get_result_from_dynamodb_layer_src_dir
  output_path = var.get_result_from_dynamodb_layer_zip_output_path
}

data "aws_iam_policy_document" "get_result_from_dynamodb_assume_role" {
  statement {
    actions = ["sts:AssumeRole"]
    effect  = "Allow"

    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }
  }
}

data "aws_iam_policy_document" "get_result_from_dynamodb_policy_doc" {
  statement {
    actions   = ["dynamodb:Scan"]
    resources = [aws_dynamodb_table.dynamodb-table.arn]
  }
}
resource "aws_iam_policy" "get_result_from_dynamodb_policy" {
  name   = var.lambda_policy_get_result_from_dynamodb
  policy = data.aws_iam_policy_document.get_result_from_dynamodb_policy_doc.json
}
resource "aws_iam_role" "get_result_from_dynamodb_lambda_role" {
  name               = var.lambda_role_get_result_from_dynamodb
  assume_role_policy = data.aws_iam_policy_document.get_result_from_dynamodb_assume_role.json
}

resource "aws_iam_role_policy_attachment" "get_result_from_dynamodb_attachment" {
  role       = aws_iam_role.get_result_from_dynamodb_lambda_role.name
  policy_arn = aws_iam_policy.get_result_from_dynamodb_policy.arn
}

resource "aws_lambda_function" "get_result_from_dynamodb_function" {
  function_name = var.get_result_from_dynamodb_function_name
  handler       = var.get_result_from_dynamodb_function_handler
  role          = aws_iam_role.get_result_from_dynamodb_lambda_role.arn
  runtime       = "python3.9"
  environment {
    variables = {
      dynamodb_table_name = data.aws_dynamodb_table.dynamodb-table.name
    }
  }

  filename         = data.archive_file.api_to_dynamodb_function_source.output_path
  source_code_hash = data.archive_file.api_to_dynamodb_function_source.output_base64sha256
  layers           = ["${aws_lambda_layer_version.api_to_dynamodb_lambda_layer.arn}"]
}

resource "aws_lambda_layer_version" "api_to_dynamodb_lambda_layer" {
  layer_name               = var.lambda_send_message_to_sqs_layer_name
  filename                 = data.archive_file.api_to_dynamodb_layer_zip.output_path
  source_code_hash         = data.archive_file.api_to_dynamodb_layer_zip.output_base64sha256
  compatible_runtimes      = ["python3.9"]
  compatible_architectures = ["x86_64"]
}

resource "aws_lambda_permission" "api_to_dynamodb_permission" {
  statement_id  = "AllowExecutionFromAPIGateway"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.get_result_from_dynamodb_function.function_name
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${aws_apigatewayv2_api.tetris_api.execution_arn}/*/*/score_evaluation"
}