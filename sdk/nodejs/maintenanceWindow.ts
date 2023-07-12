// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Maintenance window resource for a cluster.
 */
export class MaintenanceWindow extends pulumi.CustomResource {
    /**
     * Get an existing MaintenanceWindow resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: MaintenanceWindowState, opts?: pulumi.CustomResourceOptions): MaintenanceWindow {
        return new MaintenanceWindow(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'cockroach:index/maintenanceWindow:MaintenanceWindow';

    /**
     * Returns true if the given object is an instance of MaintenanceWindow.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is MaintenanceWindow {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === MaintenanceWindow.__pulumiType;
    }

    /**
     * Cluster ID
     */
    public readonly clusterId!: pulumi.Output<string>;
    /**
     * The offset duration is the duration in seconds from the beginning of each Monday (UTC) after which the maintenance window starts.
     */
    public readonly offsetDuration!: pulumi.Output<number>;
    /**
     * The window duration is the duration in seconds that the maintenance window will remain active for after it starts.
     */
    public readonly windowDuration!: pulumi.Output<number>;

    /**
     * Create a MaintenanceWindow resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: MaintenanceWindowArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: MaintenanceWindowArgs | MaintenanceWindowState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as MaintenanceWindowState | undefined;
            resourceInputs["clusterId"] = state ? state.clusterId : undefined;
            resourceInputs["offsetDuration"] = state ? state.offsetDuration : undefined;
            resourceInputs["windowDuration"] = state ? state.windowDuration : undefined;
        } else {
            const args = argsOrState as MaintenanceWindowArgs | undefined;
            if ((!args || args.clusterId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'clusterId'");
            }
            if ((!args || args.offsetDuration === undefined) && !opts.urn) {
                throw new Error("Missing required property 'offsetDuration'");
            }
            if ((!args || args.windowDuration === undefined) && !opts.urn) {
                throw new Error("Missing required property 'windowDuration'");
            }
            resourceInputs["clusterId"] = args ? args.clusterId : undefined;
            resourceInputs["offsetDuration"] = args ? args.offsetDuration : undefined;
            resourceInputs["windowDuration"] = args ? args.windowDuration : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(MaintenanceWindow.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering MaintenanceWindow resources.
 */
export interface MaintenanceWindowState {
    /**
     * Cluster ID
     */
    clusterId?: pulumi.Input<string>;
    /**
     * The offset duration is the duration in seconds from the beginning of each Monday (UTC) after which the maintenance window starts.
     */
    offsetDuration?: pulumi.Input<number>;
    /**
     * The window duration is the duration in seconds that the maintenance window will remain active for after it starts.
     */
    windowDuration?: pulumi.Input<number>;
}

/**
 * The set of arguments for constructing a MaintenanceWindow resource.
 */
export interface MaintenanceWindowArgs {
    /**
     * Cluster ID
     */
    clusterId: pulumi.Input<string>;
    /**
     * The offset duration is the duration in seconds from the beginning of each Monday (UTC) after which the maintenance window starts.
     */
    offsetDuration: pulumi.Input<number>;
    /**
     * The window duration is the duration in seconds that the maintenance window will remain active for after it starts.
     */
    windowDuration: pulumi.Input<number>;
}
