// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Information about a person user
 */
export function getPersonUser(args: GetPersonUserArgs, opts?: pulumi.InvokeOptions): Promise<GetPersonUserResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("cockroach:index/getPersonUser:getPersonUser", {
        "email": args.email,
    }, opts);
}

/**
 * A collection of arguments for invoking getPersonUser.
 */
export interface GetPersonUserArgs {
    /**
     * Email address used to find the User ID.
     */
    email: string;
}

/**
 * A collection of values returned by getPersonUser.
 */
export interface GetPersonUserResult {
    /**
     * Email address used to find the User ID.
     */
    readonly email: string;
    /**
     * User ID
     */
    readonly id: string;
}
/**
 * Information about a person user
 */
export function getPersonUserOutput(args: GetPersonUserOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetPersonUserResult> {
    return pulumi.output(args).apply((a: any) => getPersonUser(a, opts))
}

/**
 * A collection of arguments for invoking getPersonUser.
 */
export interface GetPersonUserOutputArgs {
    /**
     * Email address used to find the User ID.
     */
    email: pulumi.Input<string>;
}
