import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";
import * as awsx from "@pulumi/awsx";

const eventsQueue = new aws.sqs.Queue("serverless-python-starter-events", {
    name: "serverless-python-starter-events",
    fifoQueue: false,
    visibilityTimeoutSeconds: 1000
});

const investPriceTable = new aws.dynamodb.Table("serverless-python-starter", {
    name: "serverless-python-starter",
    attributes: [
        {
            name: "Symbol",
            type: "S",
        },
        {
            name: "Date",
            type: "S",
        },
    ],
    billingMode: "PAY_PER_REQUEST",
    hashKey: "Symbol",
    rangeKey: "Date",
});
