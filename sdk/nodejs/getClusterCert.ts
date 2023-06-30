// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * TLS certificate for the specified CockroachDB cluster. Certificates for dedicated clusters should be written to `$HOME/Library/CockroachCloud/certs/<cluster name>-ca.crt` on MacOS or Linux, or `$env:appdata\CockroachCloud\certs\<cluster name>-ca.crt` on Windows.
 *
 * Serverless clusters use the root PostgreSQL CA cert. If it isn't already installed, the certificate can be appended to `$HOME/.postgresql/root.crt` on MacOS or Linux, or `$env:appdata\postgresql\root.crt` on Windows.
 */
export function getClusterCert(args: GetClusterCertArgs, opts?: pulumi.InvokeOptions): Promise<GetClusterCertResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("cockroach:index/getClusterCert:getClusterCert", {
        "id": args.id,
    }, opts);
}

/**
 * A collection of arguments for invoking getClusterCert.
 */
export interface GetClusterCertArgs {
    /**
     * Cluster ID
     */
    id: string;
}

/**
 * A collection of values returned by getClusterCert.
 */
export interface GetClusterCertResult {
    readonly cert: string;
    /**
     * Cluster ID
     */
    readonly id: string;
}
/**
 * TLS certificate for the specified CockroachDB cluster. Certificates for dedicated clusters should be written to `$HOME/Library/CockroachCloud/certs/<cluster name>-ca.crt` on MacOS or Linux, or `$env:appdata\CockroachCloud\certs\<cluster name>-ca.crt` on Windows.
 *
 * Serverless clusters use the root PostgreSQL CA cert. If it isn't already installed, the certificate can be appended to `$HOME/.postgresql/root.crt` on MacOS or Linux, or `$env:appdata\postgresql\root.crt` on Windows.
 */
export function getClusterCertOutput(args: GetClusterCertOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetClusterCertResult> {
    return pulumi.output(args).apply((a: any) => getClusterCert(a, opts))
}

/**
 * A collection of arguments for invoking getClusterCert.
 */
export interface GetClusterCertOutputArgs {
    /**
     * Cluster ID
     */
    id: pulumi.Input<string>;
}
