// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.cockroach.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class MetricExportDatadogConfigState extends com.pulumi.resources.ResourceArgs {

    public static final MetricExportDatadogConfigState Empty = new MetricExportDatadogConfigState();

    /**
     * A Datadog API key
     * 
     */
    @Import(name="apiKey")
    private @Nullable Output<String> apiKey;

    /**
     * @return A Datadog API key
     * 
     */
    public Optional<Output<String>> apiKey() {
        return Optional.ofNullable(this.apiKey);
    }

    /**
     * Cluster ID
     * 
     */
    @Import(name="clusterId")
    private @Nullable Output<String> clusterId;

    /**
     * @return Cluster ID
     * 
     */
    public Optional<Output<String>> clusterId() {
        return Optional.ofNullable(this.clusterId);
    }

    /**
     * The Datadog region to export to
     * 
     */
    @Import(name="site")
    private @Nullable Output<String> site;

    /**
     * @return The Datadog region to export to
     * 
     */
    public Optional<Output<String>> site() {
        return Optional.ofNullable(this.site);
    }

    @Import(name="status")
    private @Nullable Output<String> status;

    public Optional<Output<String>> status() {
        return Optional.ofNullable(this.status);
    }

    @Import(name="userMessage")
    private @Nullable Output<String> userMessage;

    public Optional<Output<String>> userMessage() {
        return Optional.ofNullable(this.userMessage);
    }

    private MetricExportDatadogConfigState() {}

    private MetricExportDatadogConfigState(MetricExportDatadogConfigState $) {
        this.apiKey = $.apiKey;
        this.clusterId = $.clusterId;
        this.site = $.site;
        this.status = $.status;
        this.userMessage = $.userMessage;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(MetricExportDatadogConfigState defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private MetricExportDatadogConfigState $;

        public Builder() {
            $ = new MetricExportDatadogConfigState();
        }

        public Builder(MetricExportDatadogConfigState defaults) {
            $ = new MetricExportDatadogConfigState(Objects.requireNonNull(defaults));
        }

        /**
         * @param apiKey A Datadog API key
         * 
         * @return builder
         * 
         */
        public Builder apiKey(@Nullable Output<String> apiKey) {
            $.apiKey = apiKey;
            return this;
        }

        /**
         * @param apiKey A Datadog API key
         * 
         * @return builder
         * 
         */
        public Builder apiKey(String apiKey) {
            return apiKey(Output.of(apiKey));
        }

        /**
         * @param clusterId Cluster ID
         * 
         * @return builder
         * 
         */
        public Builder clusterId(@Nullable Output<String> clusterId) {
            $.clusterId = clusterId;
            return this;
        }

        /**
         * @param clusterId Cluster ID
         * 
         * @return builder
         * 
         */
        public Builder clusterId(String clusterId) {
            return clusterId(Output.of(clusterId));
        }

        /**
         * @param site The Datadog region to export to
         * 
         * @return builder
         * 
         */
        public Builder site(@Nullable Output<String> site) {
            $.site = site;
            return this;
        }

        /**
         * @param site The Datadog region to export to
         * 
         * @return builder
         * 
         */
        public Builder site(String site) {
            return site(Output.of(site));
        }

        public Builder status(@Nullable Output<String> status) {
            $.status = status;
            return this;
        }

        public Builder status(String status) {
            return status(Output.of(status));
        }

        public Builder userMessage(@Nullable Output<String> userMessage) {
            $.userMessage = userMessage;
            return this;
        }

        public Builder userMessage(String userMessage) {
            return userMessage(Output.of(userMessage));
        }

        public MetricExportDatadogConfigState build() {
            return $;
        }
    }

}
