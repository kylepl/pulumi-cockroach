// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.cockroach;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class MetricExportCloudwatchConfigArgs extends com.pulumi.resources.ResourceArgs {

    public static final MetricExportCloudwatchConfigArgs Empty = new MetricExportCloudwatchConfigArgs();

    /**
     * The customized AWS CloudWatch log group name.
     * 
     */
    @Import(name="logGroupName")
    private @Nullable Output<String> logGroupName;

    /**
     * @return The customized AWS CloudWatch log group name.
     * 
     */
    public Optional<Output<String>> logGroupName() {
        return Optional.ofNullable(this.logGroupName);
    }

    /**
     * The IAM role used to upload metric segments to the target AWS account.
     * 
     */
    @Import(name="roleArn", required=true)
    private Output<String> roleArn;

    /**
     * @return The IAM role used to upload metric segments to the target AWS account.
     * 
     */
    public Output<String> roleArn() {
        return this.roleArn;
    }

    /**
     * The specific AWS region that the metrics will be exported to.
     * 
     */
    @Import(name="targetRegion")
    private @Nullable Output<String> targetRegion;

    /**
     * @return The specific AWS region that the metrics will be exported to.
     * 
     */
    public Optional<Output<String>> targetRegion() {
        return Optional.ofNullable(this.targetRegion);
    }

    private MetricExportCloudwatchConfigArgs() {}

    private MetricExportCloudwatchConfigArgs(MetricExportCloudwatchConfigArgs $) {
        this.logGroupName = $.logGroupName;
        this.roleArn = $.roleArn;
        this.targetRegion = $.targetRegion;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(MetricExportCloudwatchConfigArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private MetricExportCloudwatchConfigArgs $;

        public Builder() {
            $ = new MetricExportCloudwatchConfigArgs();
        }

        public Builder(MetricExportCloudwatchConfigArgs defaults) {
            $ = new MetricExportCloudwatchConfigArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param logGroupName The customized AWS CloudWatch log group name.
         * 
         * @return builder
         * 
         */
        public Builder logGroupName(@Nullable Output<String> logGroupName) {
            $.logGroupName = logGroupName;
            return this;
        }

        /**
         * @param logGroupName The customized AWS CloudWatch log group name.
         * 
         * @return builder
         * 
         */
        public Builder logGroupName(String logGroupName) {
            return logGroupName(Output.of(logGroupName));
        }

        /**
         * @param roleArn The IAM role used to upload metric segments to the target AWS account.
         * 
         * @return builder
         * 
         */
        public Builder roleArn(Output<String> roleArn) {
            $.roleArn = roleArn;
            return this;
        }

        /**
         * @param roleArn The IAM role used to upload metric segments to the target AWS account.
         * 
         * @return builder
         * 
         */
        public Builder roleArn(String roleArn) {
            return roleArn(Output.of(roleArn));
        }

        /**
         * @param targetRegion The specific AWS region that the metrics will be exported to.
         * 
         * @return builder
         * 
         */
        public Builder targetRegion(@Nullable Output<String> targetRegion) {
            $.targetRegion = targetRegion;
            return this;
        }

        /**
         * @param targetRegion The specific AWS region that the metrics will be exported to.
         * 
         * @return builder
         * 
         */
        public Builder targetRegion(String targetRegion) {
            return targetRegion(Output.of(targetRegion));
        }

        public MetricExportCloudwatchConfigArgs build() {
            $.roleArn = Objects.requireNonNull($.roleArn, "expected parameter 'roleArn' to be non-null");
            return $;
        }
    }

}